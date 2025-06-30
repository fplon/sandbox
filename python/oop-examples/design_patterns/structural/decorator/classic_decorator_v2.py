"""
...now with composition instead of inheritance
"""

from typing import Any


class Transaction:
    def process(self) -> Any:
        raise NotImplementedError()


class BasicTransaction(Transaction):
    def process(self) -> Any:
        return "Basic transaction processed"


class TransactionLoggerDecorator:
    def __init__(self, transaction: Transaction):
        self._transaction = transaction

    def process(self) -> Any:
        result = self._transaction.process()
        self._log_transaction(result)
        return result

    def _log_transaction(self, result: Any) -> None:
        print(f"Transaction logged: {result}")


# Example usage
basic_transaction = BasicTransaction()
logged_transaction = TransactionLoggerDecorator(basic_transaction)
result = logged_transaction.process()
print(result)
