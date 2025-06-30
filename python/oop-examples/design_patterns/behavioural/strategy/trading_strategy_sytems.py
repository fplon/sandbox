from typing import Protocol


# Define the strategy interface for trading algorithms
class TradingStrategy(Protocol):
    def execute_trade(self, symbol: str, quantity: int, **kwargs) -> None: ...


# Concrete implementation of TradingStrategy for a simple buy-and-hold strategy
class BuyAndHoldStrategy:
    def execute_trade(self, symbol: str, quantity: int, price: float, **kwargs) -> None:
        total_cost = quantity * price
        print(
            f"Buying {quantity} shares of {symbol} at ${price:.2f} each, total cost: ${total_cost:.2f}."
        )


# Concrete implementation of TradingStrategy for a momentum trading strategy
class MomentumTradingStrategy:
    def execute_trade(
        self, symbol: str, quantity: int, momentum: float, **kwargs
    ) -> None:
        print(
            f"Executing momentum trade for {quantity} shares of {symbol} with momentum {momentum}."
        )


# Concrete implementation of TradingStrategy for a mean reversion trading strategy
class MeanReversionTradingStrategy:
    def execute_trade(
        self, symbol: str, quantity: int, mean_price: float, **kwargs
    ) -> None:
        print(
            f"Executing mean reversion trade for {quantity} shares of {symbol} around mean price ${mean_price:.2f}."
        )


# Context class for the trading system
class TradingSystem:
    def __init__(self, trading_strategy: TradingStrategy) -> None:
        self._trading_strategy = trading_strategy

    def set_trading_strategy(self, trading_strategy: TradingStrategy) -> None:
        self._trading_strategy = trading_strategy

    def execute_trade(self, symbol: str, quantity: int, **kwargs) -> None:
        self._trading_strategy.execute_trade(symbol, quantity, **kwargs)


if __name__ == "__main__":
    # Client code
    buy_and_hold_strategy = BuyAndHoldStrategy()
    momentum_trading_strategy = MomentumTradingStrategy()
    mean_reversion_strategy = MeanReversionTradingStrategy()

    # Trading system using the buy-and-hold strategy
    trading_system = TradingSystem(buy_and_hold_strategy)
    trading_system.execute_trade(
        "AAPL", 100, price=150.0
    )  # Output: Buying 100 shares of AAPL at $150.00 each, total cost: $15000.00.

    # Switching to momentum trading strategy
    trading_system.set_trading_strategy(momentum_trading_strategy)
    trading_system.execute_trade(
        "GOOGL", 50, momentum=0.75
    )  # Output: Executing momentum trade for 50 shares of GOOGL with momentum 0.75.

    # Switching to mean reversion trading strategy
    trading_system.set_trading_strategy(mean_reversion_strategy)
    trading_system.execute_trade(
        "MSFT", 75, mean_price=200.0
    )  # Output: Executing mean reversion trade for 75 shares of MSFT around mean price $200.00.
