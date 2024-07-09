from abc import ABC


class Entity(ABC):
    def __init__(self, x, y, speed=None, hp=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.hp = hp
        self.current_path = None
