def singleton(cls):
    _instances = {}

    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton
class Logger:
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
