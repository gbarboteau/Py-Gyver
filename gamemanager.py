"""Allow the creation of an instance of GameManager"""
import sys
import pygame

import maze
import entity


class GameManager:
    """An instance of gamemanager.py handles evrything
    happening in the game. It controls the map,
    the player, the win/lose conditions, and the
    closing of the program.
    """
    def __init__(self, path):
        """Creates an instance of GameManager, which contains
        instances of Maze, McGyver and the guardian.
        """
        self.maze = maze.Maze(path)
        self.mcgyver = entity.McGyver(self.maze.find_something("m"), "McGyver", "assets/MacGyver.png")
        self.guardian = entity.Entity(self.maze.find_something("g"), "Guardian", "assets/Guardian.png")
        self.is_playing = True

    def play_g(self):
        """Launches only if the game uses the graphic mode.
        Handles the inputs and the graphic display.
        """
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        images = {}
        for i in entity.ENTITIES:
            images[i.char] = i.sprite
        wall = pygame.image.load("assets/Wall.png")
        floor = pygame.image.load("assets/Floor.png")
        font = pygame.font.SysFont("comicsansms", 30)
        end_string = " "
        end_text = font.render(end_string, True, (0, 0, 255))
        quit_text = font.render("Press ESC to quit", True, (0, 0, 255))

        while 1:
            for y in range(0, 15):
                for x in range(0, 15):
                    if self.maze.level[y][x] == "x":
                        screen.blit(wall, (x*48, y*48))
                    else:
                        screen.blit(floor, (x*48, y*48))
                        if self.maze.level[y][x] != " ":
                            screen.blit(pygame.image.load(images.get(self.maze.level[y][x])), (x*48, y*48))

            if self.is_playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()
                        if event.key == pygame.K_LEFT:
                            self.movement((-1, 0))
                        if event.key == pygame.K_RIGHT:
                            self.movement((1, 0))
                        if event.key == pygame.K_UP:
                            self.movement((0, -1))
                        if event.key == pygame.K_DOWN:
                            self.movement((0, 1))
            else:
                if self.has_won():
                    end_string = "You won!"
                else:
                    end_string = "You lose! You forgot to pick up something..."
                for event in pygame.event.get():
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                end_text = font.render(end_string, True, (0, 0, 255))
                screen.blit(end_text, (100, 360))
                screen.blit(quit_text, (100, 410))

            item_left_text = font.render(str(len(self.maze.item_list)) + " item left", True, (0, 0, 255))
            screen.blit(item_left_text, (0, 0))
            pygame.display.flip()

    def play_t(self):
        """Launches only if the game uses the terminal mode.
        Handles the inputs and the information display.
        """
        print("\n")
        self.maze.print_level()
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
                self.maze.print_level()
                print("\nYour current position is " + str(self.mcgyver.position))
                print("You have " + str(len(self.mcgyver.inventory)) +" item, " + str(len(self.maze.item_list)) + " item remaining\n")
                user_input = input("Enter a direction to move, Q to quit\n")
            else:
                if self.has_won():
                    print("You won! That's amazing!\n")
                else:
                    print("You lose! You forgot to pick up something, try again.\n")
                user_input = input("Thank you for playing, Q to quit\n")

    def movement(self, direction):
        """Handles player movement:
        if there isn't a wall, the player is allowed to
        move. Otherwise, noting happens.
        """
        target_position = (self.mcgyver.position[0] + direction[0], self.mcgyver.position[1] + direction[1])
        previous_position = self.mcgyver.position
        print(target_position)
        if self.maze.is_there_walls(self.mcgyver.position, direction):
            print("You can't move, there's a wall!")
        else:
            if not self.maze.check_something(target_position, " ") and not self.maze.check_something(target_position, "x"):
                if self.maze.check_something(target_position, "g"):
                    self.is_playing = False
                else:
                    self.mcgyver.inventory.append(self.maze.pick_item(target_position))
            self.mcgyver.move(direction)
            self.maze.update_level(previous_position, self.mcgyver.position)

    def has_won(self):
        """Is called when the player touches the guardian.
        Returns True if every item has been collected,
        False otherwise.
        """
        self.is_playing = False
        return len(self.maze.item_list) <= 0
