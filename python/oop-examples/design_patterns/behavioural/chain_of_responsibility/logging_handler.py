from enum import Enum, auto
from typing import Optional


# Enum for log levels
class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()


# Abstract Handler class
class AbstractHandler:
    def __init__(self, next_handler: Optional["AbstractHandler"] = None):
        self.next_handler = next_handler

    def handle(self, level: LogLevel, message: str) -> None:
        if self.next_handler:
            self.next_handler.handle(level, message)


# Concrete Handler for handling DEBUG messages
class DebugHandler(AbstractHandler):
    def handle(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.DEBUG:
            print(f"[DEBUG] {message}")
        else:
            super().handle(level, message)


# Concrete Handler for handling INFO messages
class InfoHandler(AbstractHandler):
    def handle(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.INFO:
            print(f"[INFO] {message}")
        else:
            super().handle(level, message)


# Concrete Handler for handling WARNING messages
class WarningHandler(AbstractHandler):
    def handle(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.WARNING:
            print(f"[WARNING] {message}")
        else:
            super().handle(level, message)


# Concrete Handler for handling ERROR messages
class ErrorHandler(AbstractHandler):
    def handle(self, level: LogLevel, message: str) -> None:
        if level == LogLevel.ERROR:
            print(f"[ERROR] {message}")
        else:
            super().handle(level, message)


# Client code
if __name__ == "__main__":
    # Create handler chain
    error_handler = ErrorHandler()
    warning_handler = WarningHandler(error_handler)
    info_handler = InfoHandler(warning_handler)
    debug_handler = DebugHandler(info_handler)

    # Test logging
    debug_handler.handle(LogLevel.DEBUG, "This is a debug message")
    debug_handler.handle(LogLevel.INFO, "This is an info message")
    debug_handler.handle(LogLevel.WARNING, "This is a warning message")
    debug_handler.handle(LogLevel.ERROR, "This is an error message")
