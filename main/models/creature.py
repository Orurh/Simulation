from abc import ABC

from models.entity import Entity


class Creature(Entity, ABC):
    def __init__(self, x, y, speed, hp):
        super().__init__(x, y)
        self.speed = speed
        self.hp = hp

    def get_speed(self):
        return self.speed

    def increase_hp(self, amount):
        self.hp += amount

    def decrease_hp(self, amount):
        self.hp -= amount

    def is_dead(self):
        return self.hp <= 0
