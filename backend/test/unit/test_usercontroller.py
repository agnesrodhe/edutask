import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.controllers.usercontroller import UserController


@pytest.mark.unit
def test_get_user_by_email_one_match():
        user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}]
        mockedsut = sut(user)
        getuser = mockedsut.get_user_by_email(email='test@test.com')
        assert getuser == {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}

@pytest.mark.unit
def test_get_user_by_email_multiple_matches():
        user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}, {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}]
        mockedsut = sut(user)
        getuser = mockedsut.get_user_by_email(email='test@test.com')
        assert getuser == {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}

@pytest.mark.unit
def test_get_user_by_email_no_match():
        user = []
        mockedsut = sut(user)
        getuser = mockedsut.get_user_by_email(email='test@test.com')
        assert getuser == None

@pytest.mark.unit
def test_get_user_by_email_invalid_adress():
        user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}]
        mockedsut = sut(user)
        with pytest.raises(ValueError):
            mockedsut.get_user_by_email(email='test.test.com')

@pytest.mark.unit
def test_get_user_by_email_invalid_address_failed_db():
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = Exception
        mockedsut = UserController(dao=mockedDAO)
        with pytest.raises(Exception):
            mockedsut.get_user_by_email(email='test.test.com')

def sut(user: list):
        mockedDAO = mock.MagicMock()
        mockedDAO.find.return_value = user
        mockedsut = UserController(dao=mockedDAO)
        return mockedsut