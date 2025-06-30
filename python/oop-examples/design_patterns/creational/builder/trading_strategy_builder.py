"""
- We have a TradingStrategy class representing a trading strategy with attributes such as
name and parameters.
- We define an abstract StrategyBuilder class with methods for setting different parameters
of the trading strategy.
- We implement a concrete builder MovingAverageCrossoverStrategyBuilder that constructs a
moving average crossover strategy by implementing the StrategyBuilder interface.
- We have a StrategyCreator class that takes a builder and orchestrates the construction
process.
- The client code creates an instance of MovingAverageCrossoverStrategyBuilder, passes it
to StrategyCreator, and uses it to create a moving average crossover strategy.


This implementation of the Builder pattern allows us to construct complex trading strategies
with different parameters, while keeping the construction process encapsulated and separate
from the representation of the trading strategy. It provides flexibility and allows for easy
creation of different variations of trading strategies.

"""

from typing import Dict, Any

from abc import ABC, abstractmethod


# Product representation
class TradingStrategy:
    def __init__(self, name: str, parameters: Dict[str, Any]) -> None:
        self.name = name
        self.parameters = parameters


# Abstract builder
class StrategyBuilder(ABC):
    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def set_parameters(self, parameters: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    def build(self) -> TradingStrategy:
        pass


# Concrete builder for moving average crossover strategy
class MovingAverageCrossoverStrategyBuilder(StrategyBuilder):
    def __init__(self) -> None:
        self.name = ""
        self.parameters = {}

    def set_name(self, name: str) -> None:
        self.name = name

    def set_parameters(self, parameters: Dict[str, Any]) -> None:
        self.parameters = parameters

    def build(self) -> TradingStrategy:
        return TradingStrategy(self.name, self.parameters)


# Concrete builder for mean reversion strategy
class MeanReversionStrategyBuilder(StrategyBuilder):
    def __init__(self) -> None:
        self.name = ""
        self.parameters = {}

    def set_name(self, name: str) -> None:
        self.name = name

    def set_parameters(self, parameters: Dict[str, Any]) -> None:
        # Transform parameters
        if "lookback" in parameters:
            self.parameters["lookback_period"] = parameters["lookback"]
        if "threshold" in parameters:
            self.parameters["threshold"] = parameters["threshold"]

    def build(self) -> TradingStrategy:
        return TradingStrategy(self.name, self.parameters)


# Director
class StrategyCreator:
    def __init__(self, builder: StrategyBuilder) -> None:
        self.builder = builder

    def create_strategy(self, name: str, parameters: Dict[str, Any]) -> TradingStrategy:
        self.builder.set_name(name)
        self.builder.set_parameters(parameters)
        return self.builder.build()


# Usage
if __name__ == "__main__":
    moving_average_builder = MovingAverageCrossoverStrategyBuilder()
    mean_reversion_builder = MeanReversionStrategyBuilder()

    moving_average_creator = StrategyCreator(moving_average_builder)
    mean_reversion_creator = StrategyCreator(mean_reversion_builder)

    moving_average_strategy = moving_average_creator.create_strategy(
        "Moving Average Crossover",
        {"period": 50, "short_window": 20, "long_window": 50},
    )
    mean_reversion_strategy = mean_reversion_creator.create_strategy(
        "Mean Reversion", {"lookback": 30, "threshold": 2.0}
    )

    print(moving_average_strategy.name)
    print(moving_average_strategy.parameters)

    print(mean_reversion_strategy.name)
    print(mean_reversion_strategy.parameters)
