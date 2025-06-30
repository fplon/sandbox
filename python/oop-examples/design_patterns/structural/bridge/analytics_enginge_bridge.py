from abc import ABC, abstractmethod
from typing import List, Union
import numpy as np
import tensorflow as tf


# Abstraction interface for financial analytics algorithm
class FinancialAnalyticsAlgorithm(ABC):
    @abstractmethod
    def calculate_present_value(
        self, cashflows: np.ndarray, discount_rate: float
    ) -> float:
        pass


# Implementor interface for numerical computation library
class NumericalComputationLibrary(ABC):
    @abstractmethod
    def sum(self, array: np.ndarray) -> float:
        pass


# Concrete implementation using NumPy
class NumPyLibrary(NumericalComputationLibrary):
    def sum(self, array: np.ndarray) -> float:
        return np.sum(array)


# Concrete implementation using TensorFlow
class TensorFlowLibrary(NumericalComputationLibrary):
    def sum(self, array: np.ndarray) -> float:
        return tf.reduce_sum(array).numpy()


# Refined Abstraction for calculating present value
class PresentValueCalculator(FinancialAnalyticsAlgorithm):
    def __init__(self, computation_library: NumericalComputationLibrary) -> None:
        self._computation_library = computation_library

    def calculate_present_value(
        self, cashflows: np.ndarray, discount_rate: float
    ) -> float:
        discounted_cashflows = cashflows / (
            (1 + discount_rate) ** np.arange(len(cashflows))
        )
        return self._computation_library.sum(discounted_cashflows)


# Client code
if __name__ == "__main__":
    cashflows = np.array([100, 200, 300, 400, 500])
    discount_rate = 0.05

    # Using NumPy for calculations
    numpy_library = NumPyLibrary()
    present_value_calculator_numpy = PresentValueCalculator(numpy_library)
    npv_numpy = present_value_calculator_numpy.calculate_present_value(
        cashflows, discount_rate
    )
    print("Present value using NumPy:", npv_numpy)

    # Using TensorFlow for calculations
    tensorflow_library = TensorFlowLibrary()
    present_value_calculator_tf = PresentValueCalculator(tensorflow_library)
    npv_tf = present_value_calculator_tf.calculate_present_value(
        cashflows, discount_rate
    )
    print("Present value using TensorFlow:", npv_tf)
