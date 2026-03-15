"""
1. Keeping constants in one place.
2. This will avoid magical numbers (Which may not convey much meaning) in the code.
"""

# Window / grid settings
TITLE = "Snake++"
GRID_SIZE = 24 # Size of each grid cell in pixels
GRID_W = 28 # Number of grid cells in width
GRID_H = 20 # Number of grid cells in height

WIDTH = GRID_SIZE * GRID_W # Total width of the window in pixels
HEIGHT = GRID_SIZE * GRID_H # Total height of the window in pixels
FPS = 60 # Frames per second, controls the speed of the game loop

# Game pace
MOVE_EVERY_MS = 110 # Snake moves every 110 milliseconds, controls the speed of the snake
SCORE_PER_FOOD = 10 # Points awarded for eating food

# Pickup
POWERUP_CHANCE = 0.15 # Chance of a powerup spawning instead of regular food
MAX_OBSTACLES = 18 # Maximum number of obstacles that can be present on the grid at once