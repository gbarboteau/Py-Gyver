class Character:
    def __init__(self, position):
        self.x = position[1]
        self.y = position[0]
        self.position = (self.x, self.y)

class McGyver(Character):
    pass

class Guardian(Character):
    pass
