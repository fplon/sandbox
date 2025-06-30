import pytest
from unittest.mock import MagicMock
from your_module import (
    DatabaseAuthenticator,
    RbacAuthoriser,
    AuthenticationService,
    AuthorisationService,
)


# Tests for DatabaseAuthenticator
def test_database_authenticator_authenticate():
    authenticator = DatabaseAuthenticator()
    assert authenticator.authenticate("username", "password") == True


# Tests for RbacAuthoriser
def test_rbac_authoriser_has_permission():
    authoriser = RbacAuthoriser()
    assert authoriser.has_permission("admin", "read") == True
    assert authoriser.has_permission("user", "read") == True
    assert authoriser.has_permission("user", "write") == True
    assert authoriser.has_permission("user", "delete") == False


# Tests for AuthenticationService
def test_authentication_service_login():
    authenticator_mock = MagicMock()
    authenticator_mock.authenticate.return_value = True
    authentication_service = AuthenticationService(authenticator_mock)
    assert authentication_service.login("username", "password") == True
    authenticator_mock.authenticate.assert_called_once_with("username", "password")


# Tests for AuthorisationService
def test_authorisation_service_check_permission():
    authoriser_mock = MagicMock()
    authoriser_mock.has_permission.return_value = True
    authorisation_service = AuthorisationService(authoriser_mock)
    assert authorisation_service.check_permission("user", "read") == True
    authoriser_mock.has_permission.assert_called_once_with("user", "read")


# # Test main function
# def test_main(capsys):
#     # main()
#     captured = capsys.readouterr()
#     assert "Authentication successful" in captured.out


# if __name__ == "__main__":
#     pytest.main()
