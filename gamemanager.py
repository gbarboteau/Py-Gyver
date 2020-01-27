import sys
import pygame

import maze
import character


class GameManager:
    def __init__(self, path):
        self.maze = maze.Maze(path)
        self.mcgyver = character.McGyver(self.maze.find_something("m"), "assets/MacGyver.png")
        self.guardian = character.Guardian(self.maze.find_something("g"), "assets/Guardian.png")
        self.is_playing = True

    def play_g(self):
        pygame.init()
        screen = pygame.display.set_mode((720, 720))
        images = {"m" : "assets/MacGyver.png", "g" : "assets/Guardian.png", "e" : "assets/Ether.png", "n" : "assets/Needle.jpg", "t" : "assets/Tube.png",}
        wall = pygame.image.load("assets/Wall.png")
        floor = pygame.image.load("assets/Floor.png")
        font = pygame.font.SysFont("comicsansms", 30)
        end_string = " "
        end_text = font.render(end_string, True, (0, 0, 255))
        quit_text = font.render("Press ESC to quit", True, (0, 0, 255))

        while 1:
            for _y in range(0, 15):
                for _x in range(0, 15):
                    if self.maze.level[_y][_x] == "x":
                        screen.blit(wall, (_x*48, _y*48))
                    else:
                        screen.blit(floor, (_x*48, _y*48))
                        if self.maze.level[_y][_x] != " ":
                            screen.blit(pygame.image.load(images.get(self.maze.level[_y][_x])), (_x*48, _y*48))

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
        self.is_playing = False
        return len(self.maze.item_list) <= 0
