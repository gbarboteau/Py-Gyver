import sys

import gamemanager


def main():
    gm = gamemanager.GameManager("level.txt")
    if len(sys.argv) < 2:
        print("erreur")
    else:
        if sys.argv[1] == "graphic":
            gm.play_g()
        elif sys.argv[1] == "terminal":
            gm.play_t()


main()
