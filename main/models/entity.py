from abc import ABC

class Entity(ABC):
    def __init__(self, x,y, speed = 0, hp = 0):
        self.x = x
        self.y = y
        self.speed = speed
        self.hp = hp
        # self.position = np.array([x, y])