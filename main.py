import sys

import gamemanager

def main():
    gm = gamemanager.GameManager("level.txt")
    if(len(sys.argv)  < 2):
        print("erreur")
    else:
        if(sys.argv[1] == "graphic"):
            print("ok")
        elif(sys.argv[1] == "terminal"):
            gm.playT()

main()