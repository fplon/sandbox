from abc import ABC, abstractmethod
from typing import Callable, Dict


class Investment(ABC):
    @abstractmethod
    def calculate_roi(self) -> float:
        pass


class Stock(Investment):
    def __init__(self, symbol: str, price: float, quantity: int):
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def calculate_roi(self) -> float:
        return (
            self.price * self.quantity
        ) * 0.1  # Dummy ROI calculation for illustration


class Bond(Investment):
    def __init__(self, issuer: str, face_value: float, interest_rate: float):
        self.issuer = issuer
        self.face_value = face_value
        self.interest_rate = interest_rate

    def calculate_roi(self) -> float:
        return (
            self.face_value * self.interest_rate
        )  # Dummy ROI calculation for illustration


class RealEstate(Investment):
    def __init__(self, property_type: str, value: float, location: str):
        self.property_type = property_type
        self.value = value
        self.location = location

    def calculate_roi(self) -> float:
        return self.value * 0.05  # Dummy ROI calculation for illustration


# Factory dictionary mapping investment types to their corresponding lambda functions
investment_factories: Dict[str, Callable[..., Investment]] = {
    "stock": lambda symbol, price, quantity: Stock(symbol, price, quantity),
    "bond": lambda issuer, face_value, interest_rate: Bond(
        issuer, face_value, interest_rate
    ),
    "real_estate": lambda property_type, value, location: RealEstate(
        property_type, value, location
    ),
}

# Usage
investment1 = investment_factories["stock"]("AAPL", 150.0, 10)
investment2 = investment_factories["bond"]("US Treasury", 1000.0, 0.05)
investment3 = investment_factories["real_estate"]("House", 500000.0, "New York")

print("ROI for investment 1:", investment1.calculate_roi())
print("ROI for investment 2:", investment2.calculate_roi())
print("ROI for investment 3:", investment3.calculate_roi())
