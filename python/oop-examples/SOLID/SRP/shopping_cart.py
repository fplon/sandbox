"""
A class should encapsulate only one aspect of functionality and should not be responsible for
multiple unrelated tasks. This principle promotes better code organization, maintainability,
and reusability.

- ShoppingCart class is responsible for managing the shopping cart (adding items, removing items).
- PriceCalculator class is responsible for calculating the total price of items in the shopping cart.
- Each class now has a single responsibility, adhering to SRP. This makes the code more modular,
easier to maintain, and allows for better separation of concerns. Additionally, the PriceCalculator
class can be reused in other parts of the codebase where total price calculation is needed.
"""

from typing import List, Tuple


class Item:
    def __init__(self, name: str, price: float) -> None:
        self.name: str = name
        self.price: float = price


class ShoppingCart:
    def __init__(self) -> None:
        self.items: List[Tuple[Item, int]] = []

    def add_item(self, item: Item, quantity: int) -> None:
        self.items.append((item, quantity))

    def remove_item(self, item: Item) -> None:
        self.items = [(i, q) for i, q in self.items if i != item]


class PriceCalculator:
    @staticmethod
    def calculate_total_price(items: List[Tuple[Item, int]]) -> float:
        total_price: float = 0
        for item, quantity in items:
            total_price += item.price * quantity
        return total_price


# Usage
item1: Item = Item("Laptop", 1000.0)
item2: Item = Item("Headphones", 100.0)

cart: ShoppingCart = ShoppingCart()
cart.add_item(item1, 1)
cart.add_item(item2, 2)
total_price: float = PriceCalculator.calculate_total_price(cart.items)
print(f"Total pirce: {total_price}")
