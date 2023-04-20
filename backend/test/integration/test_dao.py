import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.util.dao import DAO
from src.util.validators import getValidator

@pytest.fixture
def sut():
    with patch("src.util.validators.getValidator") as mockedGetValidator:
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
    validationResult = sut.create({
        "firstName": "Test",
        "lastName": "Testsson",
        "email": "test@test.com"
        })
    # validationResult = sut
    assert validationResult == {
        "firstName": "Test",
        "lastName": "Testsson",
        "email": "test@test.com"
        }
    # assert validationResult == "hej"
    
    sut.collection.drop()