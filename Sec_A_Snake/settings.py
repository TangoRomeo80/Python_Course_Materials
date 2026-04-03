# This file contains all the settings for the game.
# This ensures that we have a single source of truth that is persistent across all classes and files.

TITLE = "Snake Game"

GRID_SIZE = 24 # Size of each grid cell in pixels
GRID_W = 28 # Number of grid cells in width
GRID_H = 20 # Number of grid cells in height

SCREEN_WIDTH = GRID_SIZE * GRID_W
SCREEN_HEIGHT = GRID_SIZE * GRID_H

FPS = 60 # Frames per second. This controls how fast the game runs. Higher means faster. Lower means slower.