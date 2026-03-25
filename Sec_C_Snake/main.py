# This is the main entry point of the game.
# We try to keep this file as clean as possible, and delegate most of the work to other files (like game.py).
from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()