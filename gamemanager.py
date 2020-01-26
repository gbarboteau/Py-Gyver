import maze
import character

class GameManager:
    def __init__(self, path):
        self.maze = maze.Maze(path)
        self.mcgyver = character.McGyver(self.maze.findSomething("m"))
        self.guardian = character.Guardian(self.maze.findSomething("g"))

    def playT(self):
        print(len(self.maze.level))
        print(self.maze.findSomething("m"))
        print("\n\n\n")
        self.maze.printLevel()
        print("\n")
        userInput = input("Press Enter for another quote, Q to quit")
        while userInput.lower() != "q":
            print("\n\n\n")

            if(userInput.lower() == "left"):
                self.movement((-1, 0))
            elif(userInput.lower() == "right"):
                self.movement((1, 0))
            if(userInput.lower() == "up"):
                self.movement((0, -1))
            if(userInput.lower() == "down"):
                self.movement((0, 1))

            self.maze.printLevel()
            print("Your current position is " + str(self.mcgyver.position) + "\n")

            userInput = input("Enter a direction to move, Q to quit")

    def movement(self, direction):
        if(self.maze.isThereWalls(self.mcgyver.position, direction) == True):
            print("You can't move, there's a wall!")
        else:
            previousPosition = self.mcgyver.position
            self.mcgyver.move(direction)
            self.maze.updateLevel(previousPosition, self.mcgyver.position)