# File to contain all the snake logics
from __future__ import annotations
from settings import GRID_SIZE
import pygame
from collections import deque

class Snake:
    """Represents the snake in the game.
       We will use encapsulation. This class keeps the snake's internal data
       and behaviour together.
       Outside code should not manually manage the snake's body.
       It should call methods like set_direction() or step_forward() or draw() 
       to interact with the snake.
    """
    def __init__(self, start_x: int, start_y: int) -> None:
        # The snake will be a deque of (x, y) tuples
        # It will initially contain 3 segemnts, the head is the first element
        self._body = deque([(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)])

        # Initial direction is right
        self._dir_x = 1
        self._dir_y = 0

        # We use next direction to store the direction that will be applied in the next step, this allows us to change direction multiple times between steps without causing issues
        self._next_dir_x = 1
        self._next_dir_y = 0

    # @property allows us to access the body and head as attributes, but they are read only, we cannot modify them directly from outside the class, this is good for encapsulation and data integrity
    @property
    def body(self) -> deque[tuple[int, int]]:
        """Returns the snake's body as a deque of (x, y) tuples."""
        return self._body

    @property
    def head(self) -> tuple[int, int]:
        """Returns the position of the snake's head."""
        return self._body[0] 
    
    def set_direction(self, dx: int, dy: int) -> None:
        """Sets the snake's next direction. The direction will be applied in the next step."""
        # We prevent reversing direction, for example if we are moving right (1, 0) we cannot move left (-1, 0)
        if (dx, dy) == (-self._dir_x, -self._dir_y):
            return
        self._next_dir_x = dx
        self._next_dir_y = dy

    def step_forward(self) -> None:
        """Moves the snake one step in its current direction."""
        # Update the current direction
        self._dir_x = self._next_dir_x
        self._dir_y = self._next_dir_y

        # Calculate the new head position
        new_head = (self.head[0] + self._dir_x, self.head[1] + self._dir_y)

        # Add the new head to the body
        self._body.appendleft(new_head)

        # Remove the tail (last segment)
        self._body.pop()

    def draw(self, surface: pygame.Surface) -> None:
        """Draws the snake on the given surface."""
        for segment in self._body:
            # pygame.Rect(left, top, width, height) creates a rectangle object, we can use it to draw the snake segments as rectangles on the screen, we multiply the grid coordinates by GRID_SIZE to get pixel coordinates
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if segment == self.head:
                color = (40, 220, 90) # Bright green for the head
            else:
                color = (20, 170, 70) # Darker green for the body 
            pygame.draw.rect(surface, color, rect, border_radius=4) # border_radius makes the rectangles have rounded corners for a nicer look