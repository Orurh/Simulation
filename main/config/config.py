class GameConfig:
    speed_of_predator = 4
    hp_of_predator = 100

    def __init__(self):
        self.width = 20
        self.height = 20
        self.persent_of_rock = 5
        self.persent_of_tree = 5
        self.persent_of_grass = 10
        self.persent_of_herbivore = 4
        self.hp_of_herbivore = 10
        self.hp_of_grass = 10
        self.speed_of_grass = 0
        self.speed_of_herbivore = 1
        self.max_hp_of_herbivore = 100
        self.max_speed = max(self.speed_of_predator, self.speed_of_herbivore)
