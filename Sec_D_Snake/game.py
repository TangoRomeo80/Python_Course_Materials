import pygame

from settings import WIDTH, HEIGHT, FPS, GRID_SIZE, GRID_W, GRID_H, TITLE, MOVE_EVERY_MS
from entities import Snake

class Game:
    """
    Game is the main manager class,
    This class contains the main loop and delegatews work to other classes
    """
    def __init__(self):
        # Initialize pre installed pygame modules
        pygame.init()
        # Create the game window
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # We use a clock to control FPS and it gives dt (dt = delta time) which is the time between frames, this is useful for smooth movement
        self.clock = pygame.time.Clock()
        # Game state flag
        self.running = True
        # Handles the paused state
        self.paused = False
        # Optional grid for debugging, we can draw it on the screen to see the grid cells
        self.show_grid = True
        # Create the snake in the middle of the grid
        # This shows composition, as the game HAS a snake.
        # Composition is a design principle where a class is composed of other classes.
        self.snake = Snake(GRID_W // 2, GRID_H // 2)
        # Timer accumulator to control snake movement
        self.move_timer = 0

    # Method to handle events
    def handle_events(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False
            elif event.key == pygame.K_g:
                self.show_grid = not self.show_grid
            elif event.key == pygame.K_p:
                self.paused = not self.paused
            # Handle snake direction input, we use WASD keys or arrow keys to control the snake
            elif event.key in (pygame.K_w, pygame.K_UP):
                self.snake.set_direction(0, -1)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.snake.set_direction(0, 1)
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                self.snake.set_direction(-1, 0)
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                self.snake.set_direction(1, 0)

    # Method to update game state
    def update(self, dt_ms: int) -> None:
        if not self.paused:
            self.move_timer += dt_ms
            while self.move_timer >= MOVE_EVERY_MS:
                self.move_timer -= MOVE_EVERY_MS
                self.snake.step_forward()

    # Method to show grid for debugging
    def draw_grid(self) -> None:
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (WIDTH, y))

    # Method to render the game
    def draw(self) -> None:
        # Fill the background with gray color
        self.screen.fill((18, 18, 22))

        # Optionally draw the grid
        if self.show_grid:
            self.draw_grid()

        # Draw the snake, using the snake's built in methods
        self.snake.draw(self.screen)

        # Update the display
        pygame.display.flip()

    def run(self) -> None:
        """
        Main game loop will do the following:
        1. Handle events (input)
        2. Update game state (move snake, check collisions, etc)
        3. Render the game (draw everything on the screen)
        """
        while self.running:
            dt_ms = self.clock.tick(FPS) # This will limit the game to run at FPS and return the time between frames in milliseconds
            
            # Handle events
            for event in pygame.event.get():
                self.handle_events(event)

            # Update game state
            self.update(dt_ms)

            # Render the game
            self.draw()

        pygame.quit()