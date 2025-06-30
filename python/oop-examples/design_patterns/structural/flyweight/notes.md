Space optimisation. 

Pros:
- Memory efficiency: By sharing common states among multiple objects, the Flyweight pattern reduces memory usage, especially when dealing with a large number of similar objects.
- Performance improvement: As the shared states are reused, it can lead to performance improvements, particularly in situations where object creation and destruction are expensive operations.
- Simplified object management: The pattern separates intrinsic (shared) state from extrinsic (unique) state, making the system more manageable and reducing the complexity of individual objects.

Cons:
- Complexity: Implementing the Flyweight pattern may introduce additional complexity, especially when managing the shared state and ensuring that it remains consistent across objects.
- Reduced encapsulation: Objects may rely on external sources for some of their state, which can reduce encapsulation and increase coupling.
- Overhead: The pattern may introduce additional overhead, such as maintaining a factory to manage the creation and retrieval of flyweight objects.

Common Use Examples:
- Text processing applications: Storing character or font information for text documents, where many characters may share the same properties.
- Graphic design applications: Storing shared properties of graphical elements like color or texture.
- Game development: Managing properties of game objects that are shared across multiple instances, such as sprites or terrain tiles.

Usage in Python:
- Yes, the Flyweight pattern can be implemented in Python. Although Python is a dynamic language with built-in features like dictionary caching, which may reduce the need for explicit use of the Flyweight pattern, it can still be beneficial in certain scenarios, particularly when dealing with memory-intensive applications or large-scale systems.

Alternative Patterns:
- Singleton: If there's only one instance of a class that needs to be shared across the application, the Singleton pattern can be used.
- Prototype: If the objects are mostly similar but can have some variations, the Prototype pattern can be employed to clone existing objects.
- Object Pool: If object creation and destruction are expensive operations, the Object Pool pattern can be used to manage a pool of reusable objects.