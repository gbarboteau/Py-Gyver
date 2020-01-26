class Character:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.position = (self.x, self.y)


class McGyver(Character):
    def move(self, direction):
        futurePosition = self.position[0] + direction[0], self.position[1] + direction[1]
        self.position = self.position[0] + direction[0], self.position[1] + direction[1]
        self.x = self.position[0]
        self.y = self.position[1]


class Guardian(Character):
    pass
    