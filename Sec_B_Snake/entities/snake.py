from __future__ import annotations

import pygame
from collections import deque
from settings import GRID_SIZE

class Snake:
    """Represents the snake in the game.
       This class keeps the snake's internal data and behaviour together (Encapsulation).

       This means outside code should not manually manage the snake's body or direction.
       Instead, it should call methods on the Snake class to change its state. 
    """
    def __init__(self, start_x: int, start_y: int):
        # We store the snakes body as a queue(FIFO) of (x, y positions on the grid)
        self._body =  deque([(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]) # Start with 3 segments (head + 2 body parts)
        # Current direction
        self._dir_x = 1 # Moving right
        self._dir_y = 0
        # We store next direction to update it cleanly
        self._next_dir_x = 1
        self._next_dir_y = 0

    @property
    def body(self) -> deque[tuple[int, int]]:
        """Returns the current body segments of the snake as a deque of (x, y) positions.
            We expose the snake's body through a read-only property instead of asking outside code 
            to directlyy manipulate the attribute.
        """
        return self._body
    
    @property
    def head(self) -> tuple[int, int]:
        """Returns the current position of the snake's head."""
        return self._body[0]
    
    def set_direction(self, dx: int, dy: int) -> None:
        """Sets the next direction of the snake. 
            We use a method to change the snake's direction instead of directly setting attributes.
            This allows us to validate the input and prevent illegal moves (like reversing direction).
        """
        # Prevent reversing direction (e.g. if moving right, can't immediately move left)
        if (dx, dy) == (-self._dir_x, -self._dir_y):
            return
        self._next_dir_x = dx
        self._next_dir_y = dy

    def step_forward(self) -> None:
        """Moves the snake by one grid cell in the current direction. 
            This method updates the snake's position based on its current direction and adds a new head segment.
            It also removes the tail segment to maintain the snake's length (unless it has just eaten food).
        """
        # Apply the queued direction change
        self._dir_x = self._next_dir_x
        self._dir_y = self._next_dir_y

        # Calculate new head position
        head_x, head_y = self.head # Get current head position
        new_head = (head_x + self._dir_x, head_y + self._dir_y) # Calculate new head position based on current direction

        # Add new head to the front of the body
        self._body.appendleft(new_head) # Add new head to the front of the deque
        # Remove the tail segment to maintain length (unless we just ate food, which would be handled elsewhere)
        self._body.pop() # Remove the last segment of the deque (the tail)

    def draw(self, surface: pygame.Surface) -> None:
        """Draws the snake on the given surface. 
            This method iterates through the snake's body segments and draws a rectangle for each one.
        """
        for segment in self._body:
            x, y = segment
            # pygame.Rect(left, top, width, height) - Creates a rectangle object with the specified position and size
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE) # Create a rectangle for the segment
            if segment == self.head:
                color = (40, 220, 90) # Bright green for the head
            else:
                color = (20, 180, 70) # Darker green for the body
            pygame.draw.rect(surface, color, rect, border_radius=6) # Draw the rectangle on the surface with the specified color  
