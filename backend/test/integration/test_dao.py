import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.util.dao import DAO

import os

@pytest.fixture
@patch("src.util.dao.getValidator", autospec=True)
def sut(mockedGetValidator):
    mockedGetValidator.return_value = {
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
                    "uniqueItems": True
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

    dao = DAO("test")
    return dao

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
    # assert validationResult == "hej"
    
    sut.collection.drop()