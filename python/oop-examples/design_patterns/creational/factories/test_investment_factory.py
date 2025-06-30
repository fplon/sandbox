import pytest
from investment_factory import Stock, Bond, RealEstate, InvestmentFactory


def test_stock_calculate_roi():
    stock = Stock(symbol="AAPL", price=100.0, quantity=10)
    expected_roi = 100.0 * 10 * 0.1  # Dummy ROI calculation from your class
    assert stock.calculate_roi() == expected_roi


def test_bond_calculate_roi():
    bond = Bond(issuer="US Treasury", face_value=1000.0, interest_rate=0.05)
    expected_roi = 1000.0 * 0.05  # Dummy ROI calculation from your class
    assert bond.calculate_roi() == expected_roi


def test_real_estate_calculate_roi():
    real_estate = RealEstate(
        property_type="residential", value=500000.0, location="New York"
    )
    expected_roi = 500000.0 * 0.05  # Dummy ROI calculation from your class
    assert real_estate.calculate_roi() == expected_roi


def test_investment_factory_stock():
    stock = InvestmentFactory.create_investment(
        "stock", symbol="AAPL", price=150.0, quantity=10
    )
    assert isinstance(stock, Stock)
    assert stock.calculate_roi() == 150.0 * 10 * 0.1


def test_investment_factory_bond():
    bond = InvestmentFactory.create_investment(
        "bond", issuer="US Treasury", face_value=1000.0, interest_rate=0.05
    )
    assert isinstance(bond, Bond)
    assert bond.calculate_roi() == 1000.0 * 0.05


def test_investment_factory_real_estate():
    real_estate = InvestmentFactory.create_investment(
        "real_estate", property_type="residential", value=500000.0, location="New York"
    )
    assert isinstance(real_estate, RealEstate)
    assert real_estate.calculate_roi() == 500000.0 * 0.05


def test_investment_factory_invalid_type():
    with pytest.raises(ValueError):
        InvestmentFactory.create_investment("invalid_type")


# Optional: Parameterize tests for factory to simplify
@pytest.mark.parametrize(
    "type,kwargs,expected_class",
    [
        ("stock", {"symbol": "AAPL", "price": 150.0, "quantity": 10}, Stock),
        (
            "bond",
            {"issuer": "US Treasury", "face_value": 1000.0, "interest_rate": 0.05},
            Bond,
        ),
        (
            "real_estate",
            {"property_type": "residential", "value": 500000.0, "location": "New York"},
            RealEstate,
        ),
    ],
)
def test_investment_factory_parameterized(type, kwargs, expected_class):
    investment = InvestmentFactory.create_investment(type, **kwargs)
    assert isinstance(investment, expected_class)
