import pytest
from investment_prototype_factory import Stock, PrototypeFactory, InvestmentPrototype


@pytest.fixture
def prototype_factory() -> PrototypeFactory:
    return PrototypeFactory()


@pytest.fixture
def apple_stock() -> Stock:
    return Stock("AAPL", "Apple Inc.", 150.25)


@pytest.fixture
def google_stock() -> Stock:
    return Stock("GOOGL", "Alphabet Inc.", 2400.0)


def test_stock_clone(apple_stock: Stock) -> None:
    cloned_stock: Stock = apple_stock.clone()
    assert cloned_stock.symbol == apple_stock.symbol
    assert cloned_stock.company_name == apple_stock.company_name
    assert cloned_stock.price == apple_stock.price


def test_stock_clone_different_object(apple_stock: Stock) -> None:
    cloned_stock: Stock = apple_stock.clone()
    assert cloned_stock is not apple_stock


def test_prototype_factory_register_and_create(
    prototype_factory: PrototypeFactory, apple_stock: Stock, google_stock: Stock
) -> None:
    prototype_factory.register_prototype("apple_stock", apple_stock)
    prototype_factory.register_prototype("google_stock", google_stock)

    apple_stock_clone: InvestmentPrototype = prototype_factory.create_prototype(
        "apple_stock"
    )
    google_stock_clone: InvestmentPrototype = prototype_factory.create_prototype(
        "google_stock"
    )

    assert isinstance(apple_stock_clone, InvestmentPrototype)
    assert isinstance(google_stock_clone, InvestmentPrototype)

    assert apple_stock_clone is not apple_stock
    assert google_stock_clone is not google_stock

    assert apple_stock_clone.symbol == apple_stock.symbol
    assert apple_stock_clone.company_name == apple_stock.company_name
    assert apple_stock_clone.price == apple_stock.price

    assert google_stock_clone.symbol == google_stock.symbol
    assert google_stock_clone.company_name == google_stock.company_name
    assert google_stock_clone.price == google_stock.price


def test_prototype_factory_unregister(
    prototype_factory: PrototypeFactory, apple_stock: Stock
) -> None:
    prototype_factory.register_prototype("apple_stock", apple_stock)
    prototype_factory.unregister_prototype("apple_stock")

    with pytest.raises(ValueError):
        prototype_factory.create_prototype("apple_stock")
