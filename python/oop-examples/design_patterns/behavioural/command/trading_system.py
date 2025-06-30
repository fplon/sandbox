from abc import ABC, abstractmethod
from typing import Any, Protocol


# Command interface
class TradeCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# Concrete command for executing a buy order
class BuyCommand(TradeCommand):
    def __init__(self, symbol: str, quantity: int) -> None:
        self.symbol = symbol
        self.quantity = quantity

    def execute(self) -> None:
        print(f"Executing buy order for {self.quantity} shares of {self.symbol}")


# Concrete command for executing a sell order
class SellCommand(TradeCommand):
    def __init__(self, symbol: str, quantity: int) -> None:
        self.symbol = symbol
        self.quantity = quantity

    def execute(self) -> None:
        print(f"Executing sell order for {self.quantity} shares of {self.symbol}")


# Invoker
class TradingSystem:
    def __init__(self) -> None:
        self._commands = []

    def add_command(self, command: TradeCommand) -> None:
        self._commands.append(command)

    def execute_commands(self) -> None:
        for command in self._commands:
            command.execute()
        self._commands.clear()


# Client code
def main() -> None:
    trading_system = TradingSystem()

    # Create buy and sell commands
    buy_order = BuyCommand(symbol="AAPL", quantity=100)
    sell_order = SellCommand(symbol="MSFT", quantity=50)

    # Add commands to the trading system
    trading_system.add_command(buy_order)
    trading_system.add_command(sell_order)

    # Execute commands
    trading_system.execute_commands()


if __name__ == "__main__":
    main()
