# Main game class container file. This file will contain the main game loop.
import pygame
from settings import TITLE, WIDTH, HEIGHT, FPS, GRID_W, GRID_H, GRID_SIZE

class Game:
    """
    Game = the manager class.
    OOP idea: This class OWNS all other classes and delegates or assigns tasks to them. It is the main controller of the game.
    """
    def __init__(self):
        # initialize pygame (Built in library setup)
        pygame.init()
        pygame.display.set_caption(TITLE)

        # Create the game window surface where everythign will be rendered.
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Create a clock to control the frame rate of the game.
        self.clock = pygame.time.Clock()

        # Game states
        self.running = True # Whether the game is running or not. This will be used to control the main game loop.
        self.paused = False # Whether the game is paused or not. This will be used to control the main game loop.

        # Grid printing for debugging purposes.
        self.show_grid = True

    def handle_event(self, event: pygame.event.Event) -> None:
        """Read user input and update game state (Not game logic, just input handling)"""
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_p:
                self.paused = not self.paused
            elif event.key == pygame.K_g:
                self.show_grid = not self.show_grid
            

    def update(self) -> None:
        pass

    def draw_grid(self) -> None:
        """Draw the grid on the screen for debugging purposes."""
        # Uses pygame.draw.line(surface, color, start_pos, end_pos, width) to draw lines on the screen. The lines will be drawn every GRID_SIZE pixels.
        # Vertical lines
        for x in range(GRID_W + 1):
            pixel_x = x * GRID_SIZE
            pygame.draw.line(self.screen, (28, 28, 34), (pixel_x, 0), (pixel_x, HEIGHT))
        # Horizontal lines
        for y in range(GRID_H + 1):
            pixel_y = y * GRID_SIZE
            pygame.draw.line(self.screen, (28, 28, 34), (0, pixel_y), (WIDTH, pixel_y))

    def draw(self) -> None:
        # Fill the screen with a solid color (background color).
        self.screen.fill((18, 18, 22))

        if self.show_grid:
            self.draw_grid()

        # Push the rendered frame to the screen.
        pygame.display.flip() # This will update the entire display with the new frame we just drew.

    def run(self) -> None:
        """
        Core game loop. It will have the following structure:
        1. Handle events (input, etc.)
        2. Update game state (move characters, check for collisions, etc.)
        3. Render the game (draw everything on the screen using pygame)
        """
        while self.running:
            dt_ms = self.clock.tick(FPS) # This will limit the game to run at the specified FPS and return the time in milliseconds since the last tick.

            # Handle events (input, etc.)
            for event in pygame.event.get():
                self.handle_event(event)

            # Update game state (move characters, check for collisions, etc.)
            self.update()

            # Render the game (draw everything on the screen using pygame)
            self.draw()

        # Quit pygame when the game loop ends.
        pygame.quit()