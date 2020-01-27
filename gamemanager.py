import maze
import character


class GameManager:
    def __init__(self, path):
        self.maze = maze.Maze(path)
        self.mcgyver = character.McGyver(self.maze.findSomething("m"))
        self.guardian = character.Guardian(self.maze.findSomething("g"))
        self.is_playing = True

    def play_t(self):
        print("\n")
        self.maze.printLevel()
        user_input = input("\nEnter a direction to move, Q to quit\n")
        while user_input.lower() != "q":
            if self.is_playing:
                print("\n")
                if user_input.lower() == "left":
                    self.movement((-1, 0))
                elif user_input.lower() == "right":
                    self.movement((1, 0))
                if user_input.lower() == "up":
                    self.movement((0, -1))
                if user_input.lower() == "down":
                    self.movement((0, 1))
                self.maze.printLevel()
                print("\nYour current position is " + str(self.mcgyver.position))
                print("You have " + str(len(self.mcgyver.inventory)) +" item, " + str(len(self.maze.itemList)) + " item remaining\n")
                user_input = input("Enter a direction to move, Q to quit\n")
            else:
                if(self.hasWon()):
                    print("You won! That's amazing!\n")
                else:
                    print("You lose! You forgot to pick up something, try again.\n")
                user_input = input("Thank you for playing, Q to quit\n")

    def movement(self, direction):
        targetPosition = (self.mcgyver.position[0] + direction[0], self.mcgyver.position[1] + direction[1])
        previous_position = self.mcgyver.position
        print(targetPosition)
        if self.maze.isThereWalls(self.mcgyver.position, direction):
            print("You can't move, there's a wall!")
        else:
            if self.maze.checkSomething(targetPosition, " ") == False and self.maze.checkSomething(targetPosition, "x") == False:
                if self.maze.checkSomething(targetPosition, "g"):
                    self.is_playing = False
                else:
                    self.mcgyver.inventory.append(self.maze.pickItem(targetPosition))
            self.mcgyver.move(direction)
            self.maze.updateLevel(previous_position, self.mcgyver.position)

    def hasWon(self):
        self.is_playing = False
        if len(self.maze.itemList) <= 0:
            return True
        else:
            return False
