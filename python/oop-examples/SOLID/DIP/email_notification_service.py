"""
Suppose we have a high-level NotificationService module responsible for sending
notifications, and a low-level EmailService module responsible for sending emails.
To adhere to the Dependency Inversion Principle, we'll introduce an abstraction
(interface) called NotificationProvider, and both NotificationService and
EmailService will depend on this abstraction rather than on each other directly.

- NotificationProvider is an interface that defines the method send_notification().
- EmailService is a low-level module that implements the NotificationProvider interface.
It is responsible for sending email notifications.
- NotificationService is a high-level module that depends on the NotificationProvider
abstraction. It can use any implementation of NotificationProvider to send notifications.


"""

from abc import ABC, abstractmethod


# Abstraction (Interface) for notification provider
class NotificationProvider(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


# Low-level module: EmailService
class EmailService(NotificationProvider):
    def send_notification(self, message: str):
        print("Sending email notification:", message)


# High-level module: NotificationService
class NotificationService:
    def __init__(self, provider: NotificationProvider):
        self.provider = provider

    def send_notification(self, message: str):
        self.provider.send_notification(message)


# Example usage
def main():
    email_service = EmailService()
    notification_service = NotificationService(email_service)
    notification_service.send_notification("Hello, world!")


if __name__ == "__main__":
    main()
