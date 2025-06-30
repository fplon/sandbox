Adding behaviour without altering the class itself

## Functional Decorator

The Functional Decorator pattern in Python offers several advantages:

Modularity: Decorators allow you to modularize your code by separating concerns. You can define reusable behavior and apply it to multiple functions without modifying their implementation.
Readability: Decorators make code more readable by allowing you to express additional functionality in a concise and clear manner. They enable you to add functionality to functions without cluttering their core logic.
Separation of Concerns: Decorators promote separation of concerns by keeping the core functionality of a function separate from additional behaviors. This makes it easier to understand and maintain code.
Dynamic Behavior: Decorators enable dynamic behavior as they can modify or enhance the behavior of functions at runtime. This flexibility is especially useful in scenarios where behavior needs to be adjusted based on certain conditions or inputs.

However, there are also some disadvantages:

Implicitness: Decorators can make code harder to understand for newcomers, as they modify the behavior of functions implicitly.
Limited Composition: Composing multiple decorators can sometimes lead to unexpected behavior, especially if they depend on each other or modify the function's signature.
Debugging Complexity: Debugging code with decorators can be more complex, as it might not always be immediately clear which decorators are applied to a function and in what order.

Alternative approaches to achieving similar functionality include:

Class-based Decorators: Instead of using functions as decorators, you can define decorators as classes. This can provide more flexibility and control, especially when dealing with stateful decorators.
Higher-order Functions: Instead of using decorators, you can achieve similar functionality using higher-order functions. This involves passing functions as arguments and returning functions as results, allowing for dynamic behavior.
Aspect-Oriented Programming (AOP): AOP is a programming paradigm that allows for the separation of cross-cutting concerns, such as logging, caching, and security, from the core logic of the program. While not directly supported in Python, similar functionality can be achieved using decorators and other techniques.

Example use cases for the Functional Decorator pattern in finance-related scenarios could include:

Logging: Adding logging functionality to functions that perform financial calculations.
Caching: Caching the results of expensive financial calculations to improve performance.
Authorization: Enforcing authorization checks before executing functions that modify financial data.
Error Handling: Adding error handling and retry logic to functions that interact with financial APIs.