import pytest
from email_notification_service import EmailService, NotificationService


# Fixture for EmailService instance
@pytest.fixture
def email_service():
    return EmailService()


# Fixture for NotificationService instance with EmailService dependency
@pytest.fixture
def notification_service(email_service):
    return NotificationService(email_service)


# Test case for EmailService send_notification method
def test_email_service_send_notification(email_service, capsys):
    message = "Test email message"
    email_service.send_notification(message)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Sending email notification: {message}"


# Test case for NotificationService send_notification method
def test_notification_service_send_notification(notification_service, capsys):
    message = "Test notification message"
    notification_service.send_notification(message)
    captured = capsys.readouterr()
    assert captured.out.strip() == f"Sending email notification: {message}"


# # Test main function to check if it runs without error
# def test_main():
#     main()  # Simply check if main function runs without errors


# if __name__ == "__main__":
#     pytest.main()
