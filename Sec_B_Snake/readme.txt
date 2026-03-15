------------Deliverables------------
1. Snake moves on a grid, grows whiloe eating food.
2. There will be different pickups (Food, Poison, Speed, Shields)
3. There will be obstacles.
4. The project should be modular (i.e. different classes for different functionalities)
5. Success conditions: Codes hould be readable, modular, and extendable.

------------Architectural Requirements------------
1. Game is the manager module:
    - It created the windows,
    - Reads keyboard events,
    - Decides when the snake should move,
    - Checks coliisions and scores
    - Spawns the pickups and obstacles
2. Snake is the "actor" module:
    - Knows its body, position, direction and effects.
    - Knows how to move and grow.
    - Know how to draw itself on the screen.
3. Pickups will use polymorphism and share the same ABC(Same interface):
    - They will have a position
    - They can draw themselves on the screen
    - They will implement apply() method
    ----How pickups will use polymorphism?----
        Suppose there are four types of pickups. They will apply different effects on the snake when eaten:
        1. Food: Increases the length of the snake by 1.
        2. Poison: Decreases the length of the snake by 1.
        3. Speed: Increases the speed of the snake for a short duration.
        4. Shield: Grants the snake temporary immunity to collisions for a short duration.
        They all implement the different behaviors in their apply() method.
        This represents the use of polymorphic behaviour.

-----OOP Concepts and how they will be used-----
1. Encapsulation: We will not edit snake's body directly. We will use methods like grow(), shrink(), set_direction().
2. Inheritance: All pickups will inherit from a common ABC (Abstract Base Class) called Pickup.
3. Polymorphism: We will use polymorphism for the pickups. They will all implement the same interface but have different behaviors when applied to the snake.
4. Abstraction: Every game object should follow same shared method interface like draw() and update().
5. Composition: Snakes should stores temporary effects of pickups in internal structure.




