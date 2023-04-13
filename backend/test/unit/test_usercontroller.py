import pytest
import unittest.mock as mock
from unittest.mock import patch

from src.controllers.usercontroller import UserController

"""
email                           |   get_user_by_email()
________________________________|_________________________
                                |
match user          db not fail |   user
                                |
more than one match db not fail |   first user in list
                                |
do not match user   db not fail |   None
                                |
not valid           db not fail |   ValueError
                                |
match user              db fail |   Exception
                                |
more than one match     db fail |   Exception
                                |
do not match user       db fail |   Exception
                                |
not valid               db fail |   Exception

"""

@pytest.mark.unit
def test_get_user_by_email_one_match():
        user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}]
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = user
        mockedsut = UserController(dao=mockedDAO)
        getuser = mockedsut.get_user_by_email(email='test@test.com')
        assert getuser == {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}

@pytest.mark.unit
def test_get_user_by_email_multiple_matches():
        user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}, {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}]
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = user
        mockedsut = UserController(dao=mockedDAO)
        getuser = mockedsut.get_user_by_email(email='test@test.com')
        assert getuser == {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}

# Vi måste veta hur koden ser ut för det vi mockar för att veta vad den returnerar, tex [] eller None?
@pytest.mark.unit
def test_get_user_by_email_no_match():
        user = []
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = user
        mockedsut = UserController(dao=mockedDAO)
        getuser = mockedsut.get_user_by_email(email='test1@test.com')
        assert getuser == None

# Vilken information är nödvändig att skicka med?
@pytest.mark.unit
def test_get_user_by_email_invalid_adress():
        user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}]
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = user
        mockedsut = UserController(dao=mockedDAO)
        with pytest.raises(ValueError):
            mockedsut.get_user_by_email(email='test.test.com')

@pytest.mark.unit
def test_get_user_by_email_invalid_address_failed_db():
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = Exception
        mockedsut = UserController(dao=mockedDAO)
        with pytest.raises(Exception):
            mockedsut.get_user_by_email(email='test.test.com')