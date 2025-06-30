from typing import List, Protocol


# Define the Subject interface for market data
class MarketDataSubject(Protocol):
    def attach(self, observer: "MarketDataObserver") -> None: ...

    def detach(self, observer: "MarketDataObserver") -> None: ...

    def notify(self, symbol: str, price: float) -> None: ...


# Concrete Subject representing market data
class MarketDataProvider(MarketDataSubject):
    def __init__(self) -> None:
        self._observers: List["MarketDataObserver"] = []

    def attach(self, observer: "MarketDataObserver") -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: "MarketDataObserver") -> None:
        self._observers.remove(observer)

    def notify(self, symbol: str, price: float) -> None:
        for observer in self._observers:
            observer.update(symbol, price)


# Define the Observer interface for financial instruments
class MarketDataObserver(Protocol):
    def update(self, symbol: str, price: float) -> None: ...


# Concrete Observer representing a financial instrument
class FinancialInstrument(MarketDataObserver):
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol

    def update(self, symbol: str, price: float) -> None:
        if symbol == self.symbol:
            print(f"Received updated price for {symbol}: ${price:.2f}")


if __name__ == "__main__":
    # Create a market data provider
    market_data_provider = MarketDataProvider()

    # Create financial instruments (observers)
    apple_stock = FinancialInstrument("AAPL")
    microsoft_stock = FinancialInstrument("MSFT")

    # Attach financial instruments to the market data provider
    market_data_provider.attach(apple_stock)
    market_data_provider.attach(microsoft_stock)

    # Simulate receiving updated market data
    market_data_provider.notify("AAPL", 150.50)
    market_data_provider.notify("MSFT", 250.75)

    # Detach an observer
    market_data_provider.detach(microsoft_stock)

    # Simulate receiving updated market data again
    market_data_provider.notify("AAPL", 155.25)
    market_data_provider.notify("MSFT", 255.00)
