"""
In this example:

We define separate interfaces Authenticatable and Authorizable for handling authentication
and authorization, respectively.
We provide concrete implementations DatabaseAuthenticator and RBACAuthorizer for
these interfaces.
The AuthenticationService and AuthorizationService classes depend on the
respective interfaces, not on concrete implementations.
The main() function demonstrates how these services can be used in a realistic scenario.


By adhering to the Interface Segregation Principle, we ensure that clients
(such as AuthenticationService and AuthorizationService) depend only on the interfaces
they need, without being affected by methods they do not use.
This makes the code more modular, maintainable, and easier to extend in the future.

A violation of ISP would be to have a single interface that combines both authentication
and authorization methods. This would force clients to depend on methods they do not use,
leading to unnecessary complexity.
"""

from abc import ABC, abstractmethod


# Interface for authentication
class Authenticatable(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass


# Interface for authorization
class Authorizable(ABC):
    @abstractmethod
    def has_permission(self, role: str, action: str) -> bool:
        pass


# Authenticatable implementation
class DatabaseAuthenticator(Authenticatable):
    def authenticate(self, username: str, password: str) -> bool:
        # Logic to authenticate against a database
        return True  # Dummy implementation for demonstration


# Authorizable implementation
class RBACAuthorizer(Authorizable):
    def has_permission(self, role: str, action: str) -> bool:
        # Logic to check role-based access control
        if role == "admin":
            return True  # Admin has all permissions
        elif role == "user" and action in ["read", "write"]:
            return True  # User can read and write
        else:
            return False


# User authentication service
class AuthenticationService:
    def __init__(self, authenticator: Authenticatable):
        self.authenticator = authenticator

    def login(self, username: str, password: str) -> bool:
        return self.authenticator.authenticate(username, password)


# Authorization service
class AuthorizationService:
    def __init__(self, authorizer: Authorizable):
        self.authorizer = authorizer

    def check_permission(self, role: str, action: str) -> bool:
        return self.authorizer.has_permission(role, action)


# Example usage
def main():
    authenticator = DatabaseAuthenticator()
    authorizer = RBACAuthorizer()

    auth_service = AuthenticationService(authenticator)
    auth_result = auth_service.login("user123", "password")

    if auth_result:
        print("Authentication successful")
        authz_service = AuthorizationService(authorizer)
        permission = authz_service.check_permission("user", "read")
        if permission:
            print("User has permission to read")
        else:
            print("User does not have permission to read")
    else:
        print("Authentication failed")


if __name__ == "__main__":
    main()
