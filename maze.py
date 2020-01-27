import random
import item


class Maze:
    def __init__(self, path):
        self.level = self.create_level(path)
        self.item_list = [item.Item("needle"), item.Item("toothpaste"), item.Item("ether")]
        for i in self.item_list:
            i.position = self.set_item_position(i.char)

    def create_level(self, path):
        with open(path, 'r') as _p:
            lines = _p.readlines()
            level = []
            for _x in range(len(lines)):
                thisline = [char for char in lines[_x] if char != '\n']
                level.append(thisline)
            return level

    def print_level(self):
        for _l in self.level:
            print("".join(_l))

    def set_item_position(self, char):
        new_position = (random.randrange(15), random.randrange(15))
        if self.is_there_walls(new_position, (0, 0)):
            return self.set_item_position(char)
        else:
            self.level[new_position[1]][new_position[0]] = char
            return new_position

    def update_level(self, previous_mg_position, current_mg_position):
        _px, _py, _cx, _cy = previous_mg_position[0], previous_mg_position[1], current_mg_position[0], current_mg_position[1]
        self.level[_py][_px] = " "
        self.level[_cy][_cx] = "m"

    def pick_item(self, item_position):
        for _i in self.item_list:
            if _i.position == item_position:
                name_to_return = _i.name
                self.item_list.remove(_i)
                return name_to_return

    def find_something(self, char):
        for _x in range(len(self.level) -1):
            if char in self.level[_x]:
                return(self.level[_x].index(char), _x)

    def check_something(self, position, char):
        return self.level[position[1]][position[0]] == char

    def is_there_walls(self, current_position, direction):
        target_position = (current_position[0] + direction[0], current_position[1] + direction[1])
        return self.check_something(target_position, "x")
        