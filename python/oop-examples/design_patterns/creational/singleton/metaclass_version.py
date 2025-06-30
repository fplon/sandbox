class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        self.log_messages = []

    def log(self, message):
        self.log_messages.append(message)

    def get_logs(self):
        return self.log_messages


# Example usage
if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("test logger")

    print(logger1.get_logs())
    print(logger2.get_logs())
    print(logger1 is logger2)
    print(logger1 == logger2)
