import copy


class InvestmentPrototype:
    def clone(self) -> "InvestmentPrototype":
        # This method should be overridden by subclasses
        pass


class Stock(InvestmentPrototype):
    def __init__(self, symbol: str, company_name: str, price: float):
        self.symbol = symbol
        self.company_name = company_name
        self.price = price

    def clone(self) -> "Stock":
        # Use deepcopy to create a new instance with the same state
        return copy.deepcopy(self)


# Client code
if __name__ == "__main__":
    # Create an instance of Stock representing a specific investment
    original_stock = Stock("AAPL", "Apple Inc.", 150.25)
    print(
        "Original:",
        original_stock.symbol,
        original_stock.company_name,
        original_stock.price,
    )

    # Clone the original stock for further analysis or comparison
    cloned_stock = original_stock.clone()
    print(
        "Cloned:",
        cloned_stock.symbol,
        cloned_stock.company_name,
        cloned_stock.price,
    )

    # Modify the cloned stock (for example, for comparison purposes)
    cloned_stock.price = 155.75
    print(
        "Modified Cloned:",
        cloned_stock.symbol,
        cloned_stock.company_name,
        cloned_stock.price,
    )
