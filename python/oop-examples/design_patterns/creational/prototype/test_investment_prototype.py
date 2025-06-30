import pytest
from investment_prototype import Stock


@pytest.fixture
def original_stock() -> Stock:
    return Stock("AAPL", "Apple Inc.", 150.25)


def test_stock_clone(original_stock: Stock):
    cloned_stock: Stock = original_stock.clone()
    assert cloned_stock.symbol == original_stock.symbol
    assert cloned_stock.company_name == original_stock.company_name
    assert cloned_stock.price == original_stock.price


def test_stock_clone_independence(original_stock: Stock):
    cloned_stock: Stock = original_stock.clone()
    # Modifying cloned stock should not affect the original stock
    cloned_stock.price = 155.75
    assert cloned_stock.price != original_stock.price


def test_stock_clone_identity(original_stock: Stock):
    cloned_stock: Stock = original_stock.clone()
    # Cloned stock should be a different object
    assert cloned_stock is not original_stock
