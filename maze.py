"""Handles the Maze instance."""
import random

import entity


class Maze:
    def __init__(self, path):
        """Creates a maze, which contains a layout of the map
        (using ASCII characters), and a list of items
        (= entities) in the level.
        """
        self.level = self.create_level(path)
        self.item_list = [entity.Entity((0, 0), "Needle", "assets/Needle.jpg"), entity.Entity((0, 0), "Tube", "assets/Tube.png"), entity.Entity((0, 0), "Ether", "assets/Ether.png")]
        for i in self.item_list:
            i.position = self.set_item_position(i.char)

    def create_level(self, path):
        """Read an external text file, and creates a level
        based on it.
        """
        with open(path, 'r') as _p:
            lines = _p.readlines()
            level = []
            for x in range(len(lines)):
                thisline = [char for char in lines[x] if char != '\n']
                level.append(thisline)
            return level

    def print_level(self):
        """Draw the level (only in terminal mode)"""
        for l in self.level:
            print("".join(l))

    def set_item_position(self, char):
        """Right after their creation, gives a random
        position to every item on the map.
        """
        new_position = (random.randrange(15), random.randrange(15))
        if self.is_there_walls(new_position, (0, 0)):
            return self.set_item_position(char)
        else:
            self.level[new_position[1]][new_position[0]] = char
            return new_position

    def update_level(self, previous_mg_position, current_mg_position):
        """Update the level map when the player moves."""
        pos_x, pos_y, cur_pos_x, cur_pos_y = previous_mg_position[0], previous_mg_position[1], current_mg_position[0], current_mg_position[1]
        self.level[pos_y][pos_x] = " "
        self.level[cur_pos_y][cur_pos_x] = "m"

    def pick_item(self, item_position):
        """Let the player pick an item"""
        for i in self.item_list:
            if i.position == item_position:
                name_to_return = i.name
                i.remove_itself()
                self.item_list.remove(i)
                return name_to_return

    def find_something(self, char):
        """Find the position of a certain entity."""
        for x in range(len(self.level) -1):
            if char in self.level[x]:
                return(self.level[x].index(char), x)

    def check_something(self, position, char):
        """Check if a certain element is at a certain point."""
        return self.level[position[1]][position[0]] == char

    def is_there_walls(self, current_position, direction):
        """Check for walls at a position related to the player"""
        target_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        return self.check_something(target_position, "x")
        