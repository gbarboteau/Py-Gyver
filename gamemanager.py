import maze
import character


class GameManager:
    def __init__(self, path):
        self.maze = maze.Maze(path)
        self.mcgyver = character.McGyver(self.maze.findSomething("m"))
        self.guardian = character.Guardian(self.maze.findSomething("g"))

    def play_t(self):
        print(len(self.maze.level))
        print(self.maze.findSomething("m"))
        print("\n\n\n")
        self.maze.printLevel()
        print("\n")
        user_input = input("Press Enter for another quote, Q to quit")
        while user_input.lower() != "q":
            print("\n\n\n")

            if user_input.lower() == "left":
                self.movement((-1, 0))
            elif user_input.lower() == "right":
                self.movement((1, 0))
            if user_input.lower() == "up":
                self.movement((0, -1))
            if user_input.lower() == "down":
                self.movement((0, 1))

            self.maze.printLevel()
            print("Your current position is " + str(self.mcgyver.position) + "\n")

            user_input = input("Enter a direction to move, Q to quit")

    def movement(self, direction):
        if self.maze.isThereWalls(self.mcgyver.position, direction):
            print("You can't move, there's a wall!")
        else:
            previous_position = self.mcgyver.position
            self.mcgyver.move(direction)
            self.maze.updateLevel(previous_position, self.mcgyver.position)
