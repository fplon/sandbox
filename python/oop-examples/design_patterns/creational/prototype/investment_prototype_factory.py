from typing import Dict

import copy


class InvestmentPrototype:
    def clone(self) -> "InvestmentPrototype":
        pass


class Stock(InvestmentPrototype):
    def __init__(self, symbol: str, company_name: str, price: float) -> None:
        self.symbol = symbol
        self.company_name = company_name
        self.price = price

    def clone(self) -> "Stock":
        return copy.deepcopy(self)


class PrototypeFactory:
    def __init__(self):
        self._prototypes: Dict[str, InvestmentPrototype] = {}

    def register_prototype(self, name: str, prototype: InvestmentPrototype) -> None:
        self._prototypes[name] = prototype

    def create_prototype(self, name: str) -> InvestmentPrototype:
        prototype = self._prototypes.get(name)
        if prototype:
            return prototype.clone()
        else:
            raise ValueError(f"No prototype registered with name {name}")

    def unregister_prototype(self, name: str) -> None:
        del self._prototypes[name]


# Usage
if __name__ == "__main__":
    factory = PrototypeFactory()

    # Register prototypes
    factory.register_prototype("apple_stock", Stock("AAPL", "Apple Inc.", 150.25))
    factory.register_prototype("google_stock", Stock("GOOGL", "Alphabet Inc.", 2400.0))

    # Create prototypes using the factory
    apple_stock_clone = factory.create_prototype("apple_stock")
    print(
        "Cloned Apple Stock:",
        apple_stock_clone.symbol,
        apple_stock_clone.company_name,
        apple_stock_clone.price,
    )

    google_stock_clone = factory.create_prototype("google_stock")
    print(
        "Cloned Google Stock:",
        google_stock_clone.symbol,
        google_stock_clone.company_name,
        google_stock_clone.price,
    )
