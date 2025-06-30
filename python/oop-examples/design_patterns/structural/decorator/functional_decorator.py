from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)


def log_calculation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Performing calculation: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Calculation result: {result}")
        return result

    return wrapper


@log_calculation
def calculate_roi(investment: float, revenue: float) -> float:
    """Calculate Return on Investment (ROI)."""
    return (revenue - investment) / investment * 100


# Example usage
roi = calculate_roi(10000, 15000)
print(f"ROI: {roi}%")
