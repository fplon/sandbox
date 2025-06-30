from abc import ABC, abstractmethod
from typing import Dict


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Dict[str, int]) -> int:
        pass


class Number(Expression):
    def __init__(self, value: int) -> None:
        self.value = value

    def interpret(self, context: Dict[str, int]) -> int:
        return self.value


class Plus(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: Dict[str, int]) -> int:
        return self.left.interpret(context) + self.right.interpret(context)


class Minus(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def interpret(self, context: Dict[str, int]) -> int:
        return self.left.interpret(context) - self.right.interpret(context)


if __name__ == "__main__":
    context = {"x": 5, "y": 10}

    # Example expression: x + y - 2
    expression = Minus(Plus(Number(context["x"]), Number(context["y"])), Number(2))

    result = expression.interpret(context)
    print("Result:", result)  # Output: Result: 13
