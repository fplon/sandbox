from abc import ABC, abstractmethod


class Investment(ABC):
    @abstractmethod
    def calculate_roi(self) -> float:
        pass


class Stock(Investment):
    def __init__(self, symbol: str, price: float, quantity: int) -> None:
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def calculate_roi(self) -> float:
        # dummy implementation
        return (self.price * self.quantity) * 0.1


class Bond(Investment):
    def __init__(self, issuer: str, face_value: float, interest_rate: float) -> None:
        self.issuer = issuer
        self.face_value = face_value
        self.interest_rate = interest_rate

    def calculate_roi(self) -> float:
        # dummy implementation
        return self.face_value * self.interest_rate


class RealEstate(Investment):
    def __init__(self, property_type: str, value: float, location: str) -> None:
        self.property_type = property_type
        self.value = value
        self.location = location

    def calculate_roi(self) -> float:
        # dummy implementation
        return self.value * 0.05


class InvestmentFactory:
    @staticmethod
    def create_investment(investment_type: str, **kwargs) -> Investment:
        if investment_type == "stock":
            return Stock(**kwargs)
        elif investment_type == "bond":
            return Bond(**kwargs)
        elif investment_type == "real_estate":
            return RealEstate(**kwargs)
        else:
            raise ValueError("Invlaid investment type")


# Usage
if __name__ == "__main__":
    investment1 = InvestmentFactory.create_investment(
        "stock", symbol="AAPL", price=150.0, quantity=10
    )
    investment2 = InvestmentFactory.create_investment(
        "bond", issuer="US Treasury", face_value=1000.0, interest_rate=0.05
    )
    investment3 = InvestmentFactory.create_investment(
        "real_estate", property_type="residential", value=500000.0, location="New York"
    )

    print(investment1.calculate_roi())
    print(investment2.calculate_roi())
    print(investment3.calculate_roi())
