class Character:
    def __init__(self, position, sprite):
        self.x = position[0]
        self.y = position[1]
        self.position = (self.x, self.y)
        self.sprite = sprite


class McGyver(Character):
    def __init__(self,position, sprite):
        super().__init__(position, sprite)
        self.inventory = []

    def move(self, direction):
        futurePosition = self.position[0] + direction[0], self.position[1] + direction[1]
        self.position = self.position[0] + direction[0], self.position[1] + direction[1]
        self.x = self.position[0]
        self.y = self.position[1]


class Guardian(Character):
    pass
    