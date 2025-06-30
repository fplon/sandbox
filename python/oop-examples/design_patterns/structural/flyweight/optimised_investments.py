"""
Let's consider a scenario where we want to represent various financial
instruments, such as stocks, bonds, and ETFs (Exchange-Traded Funds),
and we want to optimize memory usage by sharing common properties like
the symbol and market exchange among similar instruments

- FinancialInstrument: Represents a financial instrument with properties
like symbol and exchange. This class serves as the flyweight object.
- FinancialInstrumentFactory: Manages the creation and retrieval of
financial instruments. It ensures that flyweight objects are shared
whenever possible.
- main(): Demonstrates the usage of the flyweight pattern by creating
various financial instruments and outputting their information.
This example illustrates how the Flyweight pattern can be applied in
the context of investing to optimize memory usage by sharing common
properties among similar financial instruments.

"""

from typing import Dict


class FinancialInstrument:
    def __init__(self, symbol: str, exchange: str):
        self.symbol = symbol
        self.exchange = exchange

    def get_info(self):
        return f"Symbol: {self.symbol}, Exchange: {self.exchange}"


class FinancialInstrumentFactory:
    _flyweights: Dict[str, FinancialInstrument] = {}

    def get_instrument(self, symbol: str, exchange: str) -> FinancialInstrument:
        key = f"{symbol}_{exchange}"
        if key not in self._flyweights:
            self._flyweights[key] = FinancialInstrument(symbol, exchange)
        return self._flyweights[key]


def main():
    factory = FinancialInstrumentFactory()

    # Creating financial instruments
    stock1 = factory.get_instrument("AAPL", "NASDAQ")
    stock2 = factory.get_instrument("GOOG", "NASDAQ")
    bond1 = factory.get_instrument("US10Y", "NYSE")
    bond2 = factory.get_instrument("US30Y", "NYSE")
    etf1 = factory.get_instrument("SPY", "NYSE")
    etf2 = factory.get_instrument("QQQ", "NASDAQ")

    # Outputting instrument info
    print(stock1.get_info())
    print(stock2.get_info())
    print(bond1.get_info())
    print(bond2.get_info())
    print(etf1.get_info())
    print(etf2.get_info())


if __name__ == "__main__":
    main()
