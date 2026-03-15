-------Deliverables-------
1. Snake moves on a grid, grows while eating food, and dies when it collides with itself or the obstacles.
2. There can be different pickups (Food, Poiison, Speed, Shields)
3. There will be obstacles on the grid that the snake must avoid.
4. The project should be modular (i.e., separate classes for Snake, Food, Obstacles, etc.)
5. Success conditions: Code should be readalbe, modular, and extendable.

---------Architectural Design Decisions---------
1. Game is going to be the manager module:
    - It will create the game window.
    - This will read keyboard events using pygame and update game states.
    - Decides when the snake should move.
    - Checks collision with the obstacles and maintain score.
    - It will spawn pickups and obstacles at random locations.
2. Snake is the actor module:
    - Knows its body, position, direction and effects of interaction with the world.
    - Knows how to move and grow / shrink.
    - Knows how to draw itself on the screen.
3. Pickups will use polymorphism and share the common ABC (Same interface):
    - They will have a position
    - They can draw themselves on screen.
    - They will implement apply() method
    ------How pickups will use polymorphism?------
    Suppose there are different types of pickups: Food, Poison, Speed, Shields. Each of these will be a subclass of a common ABC
    1. Food: Increases the length of the snake by 1.
    2. Poison: Decreases the length of the snake by 1.
    3. Speed: Increases the speed of the snake for a certain duration.
    4. Shields: Grants temporary invincibility to the snake from collisions.
    They all will be required to implement the apply() method, which will define how they affect the snake when collected.
    This represnts the usage of polymorphic behaviour.

---OOP concepts and how they are used in the project---
1. Encapsulation: We will not edit snake's body directly from the game manager. We will use methods like grow(), shrink (), set_direction().
2. Inheritance: All pickups will inherit from a common ABC, which will enforce the implementation of the apply() method.
3. Polymorphism: The game manager will treat all pickups as instances of the common ABC.
4. Abstraction: The game manager will not need to know the internal workings of how the snake moves or how the pickups affect the snake. It will just call the appropriate methods without needing to understand the details.
5. Composition: Snake should store temporary effects of pickups in internal structure.

