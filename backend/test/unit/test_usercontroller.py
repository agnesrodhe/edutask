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









#@pytest.fixture
#def sut(user: list):
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    return mockedsut
#
#@pytest.mark.unit
#@pytest.mark.parametrize('user, expected', [([{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}],
#                                             {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}),
#                                            ([{'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'},
#                                              {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}],
#                                             {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}),
#                                            ([], None) ])
#def test_get_user_by_email(sut, expected):
#    with patch('re.fullmatch') as mockfullmatch:
#        mockfullmatch.return_value = True
#        getuser = sut.get_user_by_email(email=None)
#        assert getuser == expected
#
#@pytest.mark.unit
#def test_get_user_by_email_not_valid(sut):
#    user = []
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    with patch('re.fullmatch') as mockfullmatch:
#        mockfullmatch.return_value = True
#        with pytest.raises(ValueError):
#            mockedsut.get_user_by_email(email=None)













#@pytest.mark.unit
#def test_get_user_by_email_one_match():
#    user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}]
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    with patch('re.fullmatch') as mockfullmatch:
#        mockfullmatch.return_value = True
#        user = mockedsut.get_user_by_email(email=None)
#        assert user == {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}
#
#
#@pytest.mark.unit
#def test_get_user_by_email_more_than_one_match():
#    user = [{'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'},
#            {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}]
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    with patch('re.fullmatch') as mockfullmatch:
#        mockfullmatch.return_value = True
#        user = mockedsut.get_user_by_email(email=None)
#        assert user == {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test@test.com'}
#
#
#@pytest.mark.unit
#def test_get_user_by_email_no_match():
#    user = []
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    with patch('re.fullmatch') as mockfullmatch:
#        mockfullmatch.return_value = True
#        user = mockedsut.get_user_by_email(email=None)
#        assert user == None
#
#@pytest.mark.unit
#def test_get_user_by_email_not_valid():
#    user = []
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    with patch('re.fullmatch') as mockfullmatch:
#        mockfullmatch.return_value = False
#        assert user == None
#        with pytest.raises(ValueError):
#            mockedsut.get_user_by_email(email=None)
#









#user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'},
#        {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test2@test.com'},
#        {'firstName': 'Testa', 'lastName': 'Testasson', 'email': 'test2@test.com'}]

#@pytest.fixture
#def sut():
#    user = [{'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'},
#            {'firstName': 'Testy', 'lastName': 'Testysson', 'email': 'test2@test.com'},
#            {'firstName': 'Testa', 'lastName': 'Testasson', 'email': 'test2@test.com'}]
#    mockedDAO = mock.MagicMock()
#    mockedDAO.find.return_value = user
#    mockedsut = UserController(dao=mockedDAO)
#    return mockedsut
#
#@pytest.mark.unit
#@pytest.mark.parametrize('email, expected', [('test@test.com', {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}),
#                                             ('test1@test.com', None) ])
#def test_get_user_by_email(sut, email, expected):
#    user = sut.get_user_by_email(email=email)
#    assert user == expected





#@pytest.mark.unit
#def test_get_user_by_email(sut):
#    email = 'test@test.com'
#    user = sut.get_user_by_email(email=email)
#    assert user == {'firstName': 'Test', 'lastName': 'Testsson', 'email': 'test@test.com'}
#
#@pytest.mark.unit
#def test_get_user_by_email_no_match(sut):
#    email = 'test1@test.com'
#    user = sut.get_user_by_email(email=email)
#    assert user == None
#
#@pytest.mark.unit
#def test_get_user_by_email_not_valid(sut):
#    email = 'test.test.com'
#    with pytest.raises(ValueError):
#        sut.get_user_by_email(email=email)