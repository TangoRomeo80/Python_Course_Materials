# This is the main entry point of the game.
# We try to keep it as clean as possible and delegate work to other classes.
from game import Game

if __name__ == "__main__":
    game = Game()
    game.run()