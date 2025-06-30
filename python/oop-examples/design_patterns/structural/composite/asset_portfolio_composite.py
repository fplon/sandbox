from abc import ABC, abstractmethod
from typing import List


# Component interface
class Asset(ABC):
    @abstractmethod
    def get_value(self) -> float:
        pass


# Leaf class
class Stock(Asset):
    def __init__(self, symbol: str, price: float):
        self.symbol = symbol
        self.price = price

    def get_value(self) -> float:
        return self.price


# Composite class
class Portfolio(Asset):
    def __init__(self):
        self.assets: List[Asset] = []

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    def get_value(self) -> float:
        total_value = 0.0
        for asset in self.assets:
            total_value += asset.get_value()
        return total_value


# Example usage
if __name__ == "__main__":
    stock1 = Stock("AAPL", 150.0)
    stock2 = Stock("GOOGL", 2500.0)

    portfolio = Portfolio()
    portfolio.add_asset(stock1)
    portfolio.add_asset(stock2)

    print("Portfolio Value:", portfolio.get_value())
