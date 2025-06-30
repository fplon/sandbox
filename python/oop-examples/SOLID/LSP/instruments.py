from abc import ABC, abstractmethod
from typing import List


class Instrument(ABC):
    @abstractmethod
    def calculate_price(self) -> float:
        pass


class Stock(Instrument):
    def __init__(self, symbol: str, price: float) -> None:
        self.symbol = symbol
        self.price = price

    def calculate_price(self) -> float:
        return self.price


class Option(Instrument):
    def __init__(
        self, symbol: str, underlying_price: float, strike_price: float
    ) -> None:
        self.symbol = symbol
        self.underlying_price = underlying_price
        self.strike_price = strike_price

    def calculate_price(self) -> float:
        # Assume some complex logic to calculate the option price
        return max(self.underlying_price - self.strike_price, 0)


# Function expecting a list of financial instruments and calculating their prices
def calculate_instrument_prices(instruments: List[Instrument]) -> None:
    for instrument in instruments:
        price = instrument.calculate_price()
        print(f"Price of {instrument.symbol}: {price}")


# Usage
stock = Stock("AAPL", 150.0)
option = Option("AAPL_Call", 150.0, 160.0)

# We should be able to pass a list of Stock and Option objects to calculate_instrument_prices
instruments = [stock, option]
calculate_instrument_prices(instruments)
