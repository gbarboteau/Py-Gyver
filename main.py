""" This script launches the game,
and checks which version to use
(with graphics or in the terminal)
"""
import argparse

from gamemanager import GameManagerGraphic, GameManagerTerminal


def main():
    """The main() function is executed when the
    script launches. It creates an instance of
    GameManager, and checks with version of the game
    to launch: terminal with the -t argument, or
    graphic in every other case.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--terminal", help="Launches the game in terminal mode", action="store_true")
    args = parser.parse_args()

    if args.terminal:
        gm = GameManagerTerminal("assets/level.txt")
    else:
        gm = GameManagerGraphic("assets/level.txt")
    gm.play()


main()
