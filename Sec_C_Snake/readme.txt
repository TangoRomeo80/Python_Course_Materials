------Deliverables------
1. Snake moves on a grid, grows when eating food, and dies when colliding with itself or obstacles.
2. There can be different pickups (Food, Poison, Speed, Shields).
3. There will be obstacles that the snake has to avoid.
4. The project should be modular (i.e., separate classes for Snake, Food, Obstacles, etc.).
5. The code should be readable, modular and extendable.

------Architectural Design Decisions------
1. "Game" clas is going to be the manager module:
    - It will create the game window (using pygame).
    - This will read keyboard events and update game states accordingly (using pygame).
    - Decide when the snake should move and its direction based on keyboard input.
    - It will check collisions and maintain score.
    - It will spawn the pickups and obstacles at random locations on the grid.
2. "Snake" class will represent the snake and behave like the actor module:
    - Knows its body, position, direction and effects of interaction with the world.
    - Knows how to move, and grow/shrink.
    - Knows how to draw itself on the screen (using pygame).
3. Different Pickups classes will use polymorphism and share the common ABC (Same abstract class "Pickups"):
    - They will have a poistion
    - They can draw themselves on the screen (using pygame).
    - All of them will implement the apply() method that defines how they affect the snake when eaten (Polymorphism).

---OOP concepts and how they are applied in the project---
1. Encapsulation: We will not edit snake's body directly from game mamanger. We will use methods like grow(), shrink(), set_direction() etc.
2. Inheritance: All pickups will inherit from a common ABC, which will enforce the implementation of the apply() method.
3. polymorphism: The game manager will treat all pickups as instances of the common ABC.
4. Abstraction: The game manager will not need to know the internal workings of the snake or pickups, it will just call their methods to interact with them.
5. Composition: The game is composed of snake. It shows "HAS-A" relationship.

