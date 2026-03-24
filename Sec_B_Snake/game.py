import pygame

from settings import WIDTH, HEIGHT, FPS, GRID_SIZE, GRID_W, GRID_H, TITLE, MOVE_EVERY_MS

from entities.snake import Snake

class Game:
    """
    This is the manager class.
    This class OWNS the main loop and delegates specific tasks to other classes.
    """

    def __init__(self):
        pygame.init() # Initialize pygame modules (Pre-installed library for game development)
        pygame.display.set_caption(TITLE)

        # Window surface where we will draw everything
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Game clock to control the frame rate and update timing
        self.clock = pygame.time.Clock()

        # Game status flags
        self.running = True

        # Toggle for showing grid lines (for debugging)
        self.show_grid = True

        # Initialize the snake (Game has a snake)
        # Has a relationship with the snake class (Composition)
        self.snake = Snake(GRID_W // 2, GRID_H // 2) # Start in the middle of the grid

        # Timer to control snake movement
        self.move_accumulator_ms = 0

    # Method to handle events
    def handle_events(self, event: pygame.event.Event) -> None:
        """Read user inputs and update game state accordingly."""
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_g:
                self.show_grid = not self.show_grid
            # Handle snake direction input (wasd key or arrow keys)
            elif event.key in (pygame.K_w, pygame.K_UP):
                self.snake.set_direction(0, -1) # Move up
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.snake.set_direction(0, 1) # Move down
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                self.snake.set_direction(-1, 0) # Move left
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                self.snake.set_direction(1, 0) # Move right

    # Method to update game state
    def update(self, dt_ms: int) -> None:
        # We implement timer based movement
        self.move_accumulator_ms += dt_ms
        while self.move_accumulator_ms >= MOVE_EVERY_MS:
            self.move_accumulator_ms -= MOVE_EVERY_MS # Reduce the accumulator by the move interval, allowing for multiple moves if dt_ms is large (e.g. if the game lags)
            self.snake.step_forward() # Move the snake forward by one step

    # Method to draw grid lines (for debugging)
    def draw_grid(self) -> None:
        for x in range(0, WIDTH, GRID_SIZE):
            # pygame.draw.line(surface, color, start_pos, end_pos) - Draws a line on the given surface with the specified color from start_pos to end_pos
            pygame.draw.line(self.screen, (40, 40, 45), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 45), (0, y), (WIDTH, y))

    # Method to render everything on the screen
    def render(self) -> None:
        # Fille the screen with background color
        self.screen.fill((18, 18, 22)) # Dark gray background
        # Draw grid lines if enabled
        if self.show_grid:
            self.draw_grid()

        # Draw the snake
        self.snake.draw(self.screen)

        pygame.display.flip() # Update the full display surface to the screen (Built in function)

    # Main game loop
    def run(self) -> None:
        """Main game loop structure:
        1. Handle events (Input)
        2. Update game state (Logic)
        3. Render everything (Drawing)
        """ 
        while self.running:
            # clock.tick limits the loop to run at most FPS times per second
            dt_ms = self.clock.tick(FPS) # Time in milliseconds since last tick, used for timing updates (dt = delta time)

            # 1. Handle events
            for event in pygame.event.get():
                self.handle_events(event)

            # 2. Update game state
            self.update(dt_ms)

            # 3. Render everything
            self.render()
        
        pygame.quit()
    