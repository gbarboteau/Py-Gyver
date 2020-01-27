import maze
import character
import sys, pygame


class GameManager:
    def __init__(self, path):
        self.maze = maze.Maze(path)
        self.mcgyver = character.McGyver(self.maze.findSomething("m"), "assets/MacGyver.png")
        self.guardian = character.Guardian(self.maze.findSomething("g"), "assets/Guardian.png")
        self.is_playing = True

    def play_g(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        images = {"m" : "assets/MacGyver.png", "g" : "assets/Guardian.png", "e" : "assets/Ether.png", "n" : "assets/Needle.jpg", "t" : "assets/Tube.png",}
        mcg = pygame.image.load("assets/MacGyver.png")
        wall = pygame.image.load("assets/Wall.png")
        floor = pygame.image.load("assets/Floor.png")
        while 1:
            if self.is_playing:
                for y in range(0, 15):
                    for x in range (0, 15):
                        if self.maze.level[y][x] == "x":
                            screen.blit(wall, (x*48, y*48))
                        else:
                            screen.blit(floor, (x*48, y*48))
                            if self.maze.level[y][x] != " ":
                                screen.blit(pygame.image.load(images.get(self.maze.level[y][x])), (x*48, y*48))       
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.movement((-1, 0))
                        if event.key == pygame.K_RIGHT:
                            self.movement((1, 0))
                        if event.key == pygame.K_UP:
                            self.movement((0, -1))
                        if event.key == pygame.K_DOWN:
                            self.movement((0, 1))

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

    # def draw(self, view, viewpos):
    #     for y in range(0, 640, 48):
    #         for x in range (0, 480, 48):
    #             view.blit("assets/MacGyver.png", (x, y))