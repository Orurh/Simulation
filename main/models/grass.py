from models.entity import Entity


class Grass(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "|🌿|"
