"""Handles the creation and deletion
of every entity of the game.
"""


class Entity:
    """An entity is a thing that exists in the
    game world.
    It can be an item, an enemy, or a player.
    Whatever the case, it always possesses several
    properties (a position, a sprite...) and the
    capacity to remove itself from the list of
    the game entities.
    """
    def __init__(self, position, name, sprite):
        """Creates an entity, which has a position
        (which contains x and y coordinates),
        a name, a character representing itself on
        the terminal map (the first character of its
        name), a sprite for the graphic map/
        """
        self.position = position
        self.name = name
        self.char = name[0].lower()
        self.sprite = sprite


class McGyver(Entity):
    """McGyver is our player class,a special entity:
    it inherits every traits of the Entity class,
    but can moves and is also recognized as
    the player entity by the gamemanager.
    """
    def __init__(self, position, name, sprite):
        """Creates a player instance. Has the same
        properties than other entities, but also has
        an inventory and is able to move.
        """
        super().__init__(position, name, sprite)
        self.inventory = []

    def move(self, direction):
        """Moves the player entity in its new position."""
        self.position = self.position[0] + direction[0], self.position[1] + direction[1]
