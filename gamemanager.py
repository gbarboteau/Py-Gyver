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
    Since the way the game plays and looks differs
    whether you play in terminal or graphic mode,
    the methods play() and draw() are handled in the
    mode specific classes GameManagerGraphic and
    GameManagerTerminal
    """
    def __init__(self, path):
        """Creates an instance of GameManager, which contains
        instances of Maze, McGyver and the guardian.
        The constructor remains the same for the terminal
        game manager.
        """
        self.maze = maze.Maze(path)
        self.mcgyver = entity.McGyver(self.maze.find_something("m"), "McGyver", "assets/MacGyver.png")
        self.guardian = entity.Entity(self.maze.find_something("g"), "Guardian", "assets/Guardian.png")
        self.is_playing = True

    def movement(self, direction):
        """Handles player movement:
        if there isn't a wall, the player is allowed to
        move. Otherwise, noting happens.
        """
        target_position = (self.mcgyver.position[0] + direction[0], self.mcgyver.position[1] + direction[1])
        previous_position = self.mcgyver.position
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

    def restart(self):
        """Is called when the player wants to
        restarts the game.
        """
        self.maze = maze.Maze("assets/level.txt")
        self.mcgyver = entity.McGyver(self.maze.find_something("m"), "McGyver", "assets/MacGyver.png")
        self.guardian = entity.Entity(self.maze.find_something("g"), "Guardian", "assets/Guardian.png")
        self.is_playing = True



class GameManagerGraphic(GameManager):
    """Launches only if the game is played in
    graphic mode.
    """
    def __init__(self, path):
        """Graphic assets needs to be initialized, which
        wasn't the case for its parent class.
        """
        super().__init__(path)
        pygame.init() #Pygame needs to be init if we want to use its fonctionalities
        self.screen = pygame.display.set_mode((720, 720))
        self.images = {}
        for i in entity.ENTITIES:
            self.images[i.char] = i.sprite
        self.wall = pygame.image.load("assets/Wall.png")
        self.floor = pygame.image.load("assets/Floor.png")
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.end_text = self.font.render(" ", True, (0, 0, 255))
        self.quit_text = self.font.render("Press ESC to quit", True, (0, 0, 255))

    def play(self):
        """Handles game logic and player inputs when
        the game is played in graphic mode.
        """
        while 1:
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
                        if event.key == pygame.K_r:
                            self.restart()
            else:
                if self.has_won(): 
                    self.end_text = self.font.render("You won!", True, (0, 0, 255))
                else:
                    self.end_text = self.font.render("You lose! You forgot to pick up something...", True, (0, 0, 255))
                for event in pygame.event.get():
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    elif event.key == pygame.K_r:
                        self.restart()
            self.draw(self.screen)

    def draw(self, surface):
        """Handles the display of the game.
        Is called at the end of play(), when
        every action have been taken into
        account.
        """
        for y in range(0, 15):
            for x in range(0, 15):
                if self.maze.level[y][x] == "x":
                    surface.blit(self.wall, (x*48, y*48))
                else:
                    surface.blit(self.floor, (x*48, y*48))
                    if self.maze.level[y][x] != " ":
                        surface.blit(pygame.image.load(self.images.get(self.maze.level[y][x])), (x*48, y*48))

        if not self.is_playing:
            surface.blit(self.end_text, (100, 360))
            surface.blit(self.quit_text, (100, 410))

        item_left_text = self.font.render(str(len(self.maze.item_list)) + " item left", True, (0, 0, 255))
        surface.blit(item_left_text, (0, 0))
        pygame.display.flip()


class GameManagerTerminal(GameManager):
    """Launches only if the game is played in
    terminal mode.
    """
    def play(self):
        """Launches only if the game uses the terminal mode.
        Handles the inputs and the information display.
        The draw() method seen in the GameManagerGraphic
        class doesn't exist here, as inputs and display
        are way more connected when you play directly in
        the terminal.
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
                if user_input.lower() == "r":
                    self.restart()
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
