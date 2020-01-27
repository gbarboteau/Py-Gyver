""" This script launches the game,
and checks which version to use
(with graphics or in the terminal)
"""
import sys

import gamemanager


def main():
    """The main() function is executed when the
    script launches. It creates an instance of
    GameManager, and checks with version of the game
    to launch.
    """
    gm = gamemanager.GameManager("level.txt")
    if len(sys.argv) < 2:
        gm.play_g()
    else:
        if sys.argv[1] == "graphic":
            gm.play_g()
        elif sys.argv[1] == "terminal":
            gm.play_t()
        else:
            print("Error: unknown mode")


main()
