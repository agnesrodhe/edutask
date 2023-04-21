import pytest
import json
import unittest.mock as mock
from unittest.mock import patch
from src.util.dao import DAO

from pymongo.errors import WriteError

import os

@pytest.fixture
@patch("src.util.dao.getValidator", autospec=True)
def sut(mockedGetValidator):
    validator_string = """
    {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["firstName", "lastName", "email"],
            "properties": {
                "firstName": {
                    "bsonType": "string",
                    "description": "the first name of a user must be determined"
                }, 
                "lastName": {
                    "bsonType": "string",
                    "description": "the last name of a user must be determined"
                },
                "email": {
                    "bsonType": "string",
                    "description": "the email address of a user must be determined",
                    "uniqueItems": true
                },
                "tasks": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "objectId"
                    }
                }
            }
        }
    }
    """

    mockedGetValidator.return_value = json.loads(validator_string)

    dao = DAO("test")
    yield dao

    dao.collection.drop()

@pytest.mark.integration
def test_create_document_working(sut):
    firstName = ("firstName", "Test")
    lastName = ("lastName", "Testsson")
    email = ("email", "test@test.com")

    validationResult = sut.create({
        firstName[0]: firstName[1],
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

    assert validationResult[firstName[0]] == firstName[1]
    assert validationResult[lastName[0]] == lastName[1]
    assert validationResult[email[0]] == email[1]
    
    #sut.collection.drop()

@pytest.mark.integration
def test_create_document_not_unique(sut):
    firstName = ("firstName", "Test")
    lastName = ("lastName", "Testsson")
    email = ("email", "test@test.com")

    with pytest.raises(WriteError):
        sut.create({
        firstName[0]: firstName[1],
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

        #sut.collection.drop()

@pytest.mark.integration
def test_create_document_false_bson(sut):
    firstName = ("firstName", 123)
    lastName = ("lastName", "Testsson")
    email = ("email", "test1@test.com")

    with pytest.raises(WriteError):
        sut.create({
        firstName[0]: firstName[1],
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

        #sut.collection.drop()

@pytest.mark.integration
def test_create_document_false_bson_not_unique(sut):
    firstName = ("firstName", 123)
    lastName = ("lastName", "Testsson")
    email = ("email", "test@test.com")

    with pytest.raises(WriteError):
        sut.create({
        firstName[0]: firstName[1],
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

    #sut.collection.drop()

@pytest.mark.integration
def test_create_document_not_all_required(sut):
    lastName = ("lastName", "Testsson")
    email = ("email", "test2@test.com")

    with pytest.raises(WriteError):
        sut.create({
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

    #sut.collection.drop()

@pytest.mark.integration
def test_create_document_not_all_required_not_unique(sut):
    lastName = ("lastName", "Testsson")
    email = ("email", "test@test.com")

    with pytest.raises(WriteError):
        sut.create({
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

    #sut.collection.drop()

@pytest.mark.integration
def test_create_document_not_all_required_false_bson(sut):
    lastName = ("lastName", 123)
    email = ("email", "test3@test.com")

    with pytest.raises(WriteError):
        sut.create({
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

    #sut.collection.drop()

@pytest.mark.integration
def test_create_document_not_all_required_false_bson_not_unique(sut):
    lastName = ("lastName", 123)
    email = ("email", "test@test.com")

    with pytest.raises(WriteError):
        sut.create({
        lastName[0]: lastName[1],
        email[0]: email[1],
        })

    sut.collection.drop()

