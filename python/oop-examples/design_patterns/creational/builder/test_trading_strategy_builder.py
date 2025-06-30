import pytest
from your_module import (
    TradingStrategy,
    StrategyBuilder,
    MovingAverageCrossoverStrategyBuilder,
    MeanReversionStrategyBuilder,
    StrategyCreator,
)


@pytest.fixture
def moving_average_crossover_builder():
    return MovingAverageCrossoverStrategyBuilder()


@pytest.fixture
def mean_reversion_builder():
    return MeanReversionStrategyBuilder()


def test_moving_average_crossover_strategy_builder(moving_average_crossover_builder):
    moving_average_crossover_builder.set_name("MACD")
    moving_average_crossover_builder.set_parameters(
        {"short_period": 20, "long_period": 50}
    )
    strategy = moving_average_crossover_builder.build()
    assert strategy.name == "MACD"
    assert strategy.parameters == {"short_period": 20, "long_period": 50}


def test_mean_reversion_strategy_builder(mean_reversion_builder):
    mean_reversion_builder.set_name("Mean Reversion")
    mean_reversion_builder.set_parameters({"lookback": 30, "threshold": 2.5})
    strategy = mean_reversion_builder.build()
    assert strategy.name == "Mean Reversion"
    assert strategy.parameters == {"lookback_period": 30, "threshold": 2.5}


def test_strategy_creator_with_moving_average_crossover(
    moving_average_crossover_builder,
):
    creator = StrategyCreator(moving_average_crossover_builder)
    strategy = creator.create_strategy("MACD", {"short_period": 20, "long_period": 50})
    assert strategy.name == "MACD"
    assert strategy.parameters == {"short_period": 20, "long_period": 50}


def test_strategy_creator_with_mean_reversion(mean_reversion_builder):
    creator = StrategyCreator(mean_reversion_builder)
    strategy = creator.create_strategy(
        "Mean Reversion", {"lookback": 30, "threshold": 2.5}
    )
    assert strategy.name == "Mean Reversion"
    assert strategy.parameters == {"lookback_period": 30, "threshold": 2.5}
