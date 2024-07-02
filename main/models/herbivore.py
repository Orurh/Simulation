from models.creature import Creature

class Herbivore(Creature):
    def __init__(self, x, y, speed, hp):
        super().__init__(x, y, speed, hp)

    def __str__(self):
        return "|🐑|"

    def make_move(self):
        pass