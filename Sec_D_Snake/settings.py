# This is the central configuration module
"""
This keeps constants in one place
This also avoids magical numbers in code which has no meaning to the reader
"""

# Window /grid settings
TITLE = "Snake++"
GRID_SIZE = 24 # Size of one grid cell in pixels
GRID_W = 28 # Number of grid cells in width
GRID_H = 20 # Number of grid cells in height

WIDTH = GRID_SIZE * GRID_W
HEIGHT = GRID_SIZE * GRID_H
FPS = 60

# Game Pacing
MOVE_EVERY_MS = 110 # Move every 110ms, this is the speed of the snake
SCORE_PER_FOOD = 10

# Pickups
POWERUP_CHANCE = 0.15 # Chance of a powerup spawning instead of food
MAX_OBSTACLES = 18

