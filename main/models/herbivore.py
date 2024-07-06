from models.creature import Creature

class Herbivore(Creature):


    def __str__(self):
        return "|🐑|"

    def increase_hp(self, amount):
        self.hp += amount

    def decrease_hp(self, amount):
        self.hp -= amount

    def is_dead(self):
        return self.hp <= 0