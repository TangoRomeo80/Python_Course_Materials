-------Game Features-------
1. Snake moves on a grid and grows when eating food, dies when colliding with itself or obstacles.
2. There can be different types of pickups (Food, poison, speed, shields).
3. There will obstacles on the grid that the snake must avoid.

-------Design requirements-------
1. Project should be modular and well-structured, with clear separation of concerns (i.e., separate classes for snake, pickups, obstacles).
2. Code should be readable, conform to OOP principles, and extendable.

-------Implementation design decisions-------
1. "Game" class will be the central manager module:
    - It will create the game window (Using pygame).
    - This will read keyboard events and update game states accordingly.
    - Decide when the snake moves and its directions based on keyboard inputs.
    - it will check collisions with pickups and obstacles, and maintain score.
    - it will also spawn pickups and obstacles at random locations on the grid.
2. "Snake" class will represent the snake and behave like an actor module:
    - Knows its body, position, direction and effects of interaction with the world.
    - Knows how to move, grow, and check for self-collisions.
    - Knows how to draw itself on the game window (using pygame).
3. Different pickup classes will use polymorphism and share a common ABC (Same abstract class "Pickup"):
    - They will have own position
    - They can draw themselves on the game window (using pygame).
    - All of them will implement the apply() method that defines their effect on the snake when collected.

---OOP concepts and how they will be used in this project---
1. Encapsulation: We will not edit snake's body directly from the game manager. We will use methods like grow(), shrink(), set_direction() to modify the snake.
2. Inheritance: Different types of pickups will inherit from the abstract "Pickup" class and implement their specific behaviors.
3. Polymorphism: The game manager will treat all pickups as instances of the "Pickup" class, allowing it to call the apply() method without needing to know the specific type of pickup.
4. Abstraction: The game manager will not need to know the internal workings of the snake or pickups.
5. Composition: The game is composed of snake, pickups, and obstacles. It shows "HAS-A" relationship.