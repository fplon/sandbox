import pytest
import numpy as np
from analytics_enginge_bridge import (
    NumPyLibrary,
    TensorFlowLibrary,
    PresentValueCalculator,
)


@pytest.fixture
def cashflows():
    return np.array([100, 200, 300, 400, 500])


@pytest.fixture
def discount_rate():
    return 0.05


def test_numpy_library_sum():
    numpy_library = NumPyLibrary()
    array = np.array([1, 2, 3])
    assert numpy_library.sum(array) == 6


def test_tensorflow_library_sum():
    tensorflow_library = TensorFlowLibrary()
    array = np.array([1, 2, 3])
    assert tensorflow_library.sum(array) == 6


def test_present_value_calculator_numpy(cashflows, discount_rate):
    numpy_library = NumPyLibrary()
    present_value_calculator_numpy = PresentValueCalculator(numpy_library)
    npv_numpy = present_value_calculator_numpy.calculate_present_value(
        cashflows, discount_rate
    )
    assert npv_numpy == 1288.2895  # This value is based on the calculation using NumPy


def test_present_value_calculator_tf(cashflows, discount_rate):
    tensorflow_library = TensorFlowLibrary()
    present_value_calculator_tf = PresentValueCalculator(tensorflow_library)
    npv_tf = present_value_calculator_tf.calculate_present_value(
        cashflows, discount_rate
    )
    assert (
        npv_tf == 1288.2895
    )  # This value is based on the calculation using TensorFlow
