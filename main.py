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
    if len(sys.argv) < 2:
        gm = gamemanager.GameManagerGraphic("assets/level.txt")
    else:
        if sys.argv[1] == "graphic":
            gm = gamemanager.GameManagerGraphic("assets/level.txt")
        elif sys.argv[1] == "terminal":
            gm = gamemanager.GameManagerTerminal("assets/level.txt")
        else:
            print("Error: unknown mode. Mode set automatically to 'graphic'")
            gm = gamemanager.GameManagerGraphic("assets/level.txt")
    gm.play()


main()
