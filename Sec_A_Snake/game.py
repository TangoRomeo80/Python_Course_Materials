# Main game class container file. It will contain the main game loop.
import pygame
from settings import TITLE, SCREEN_WIDTH, SCREEN_HEIGHT, FPS, GRID_H, GRID_W, GRID_SIZE

class Game:
    """
    Game is the manager class.
    OOP Idea: This class HAS all other classes and delegates or assigns work to them.
    """
    def __init__(self):
        # Initialize pygame (External library for game development)
        pygame.init()
        pygame.display.set_caption(TITLE)

        # Create the game window (Surface) and set its dimensions
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create a clock to control the frame rate of the game
        self.clock = pygame.time.Clock()

        # game states
        self.running = True # Whether the game is running or not. This will control the main game loop.
        self.paused = False # Whether the game is paused or not. This will control whether we update the game state or not.

        # Grid printing for debug purposes
        self.show_grid = True # Whether to show the grid or not. This is for debug purposes.

    def handle_events(self, event: pygame.event.Event) -> None:
        """
        This method will handle all events in the game.
        It will be called in the main game loop.
        """
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
        """
        This method will update the game state.
        It will be called in the main game loop after handling events.
        """
        pass

    def draw_grid(self) -> None:
        """
        This method will draw the grid on the screen.
        It will be called in the draw method if show_grid is True.
        """
        # Uses pygame.draw.line(surface, color, start_pos, end_pos) to draw the grid lines
        # Draw vertical lines
        for x in range(GRID_W + 1):
            pixel_x = x * GRID_SIZE
            pygame.draw.line(self.screen, (28, 28, 34), (pixel_x, 0), (pixel_x, SCREEN_HEIGHT))
        # Draw horizontal lines
        for y in range(GRID_H + 1):
            pixel_y = y * GRID_SIZE
            pygame.draw.line(self.screen, (28, 28, 34), (0, pixel_y), (SCREEN_WIDTH, pixel_y))

    def draw(self) -> None:
        """
        This method will draw the game on the screen.
        It will be called in the main game loop after updating the game state.
        """
        # Fill the screen with a background color (RGB)
        self.screen.fill((18, 18, 22))

        # Draw the grid if show_grid is True
        if self.show_grid:
            self.draw_grid()

        # Update the display to show the new frame
        pygame.display.flip()

    def run(self) -> None:
        """
        This is the main game loop. It will have the following structure:
        1. Handle events (inputs, collisions, etc.)
        2. Update the game state (move the snake, check for collisions, etc.)
        3. Render the game (draw the snake, food, etc. on the screen)
        """
        while self.running:
            dt_ms = self.clock.tick(FPS) # This will limit the game to run at the specified FPS and return the time in milliseconds since the last tick.

            # Handle events
            for event in pygame.event.get():
                self.handle_events(event)
            
            # Update the game state
            self.update()
            
            # Render the game
            self.draw()

        # Quit pygame when the game loop ends
        pygame.quit()