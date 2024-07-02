from actions.action import EntityGeneratorStrategy
from random import choice


class StaticEntityGeneratorStrategy(EntityGeneratorStrategy):
    def generate(self) -> None:
        while self.world.get_percent_of_type(self.entity_type) < self.target_percent:
            free_cells = list(self.world.get_free_cells())
            if free_cells:
                x, y = choice(free_cells)
                self.world.add_entity(self.entity_type(x, y))
            # Генерация статических объектов


class DynamicEntityGeneratorStrategy(EntityGeneratorStrategy):
    def __init__(self, world, entity_type, target_percent, speed_range, hp_range):
        super().__init__(world, entity_type, target_percent)
        self.speed_range = speed_range
        self.hp_range = hp_range

    def generate(self) -> None:
        while self.world.get_percent_of_type(self.entity_type) < self.target_percent:
            free_cells = list(self.world.get_free_cells())
            if free_cells:
                x, y = choice(free_cells)
                self.world.add_entity(self.entity_type(x, y, self.speed_range, self.hp_range))
# Генерация динамических объектов
