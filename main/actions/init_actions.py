from random import choice

from actions.action import EntityGeneratorStrategy


class StaticEntityGeneratorStrategy(EntityGeneratorStrategy):
    def __init__(self, world, entity_type, target_percent):
        super().__init__(world)
        self.entity_type = entity_type
        self.target_percent = target_percent

    def generate_or_perform_action(self) -> None:
        while self.world.get_percent_of_type(self.entity_type) < self.target_percent:
            free_cells = list(self.world.get_free_cells())
            if free_cells:
                x, y = choice(free_cells)
                self.world.add_entity(self.entity_type(x, y))
            # Генерация статических объектов


class DynamicEntityGeneratorStrategy(EntityGeneratorStrategy):
    def __init__(self, world, entity_type, target_percent, speed_range, hp_range):
        super().__init__(world)
        self.entity_type = entity_type
        self.target_percent = target_percent
        self.speed_range = speed_range
        self.hp_range = hp_range

    def generate_or_perform_action(self) -> None:
        while self.world.get_percent_of_type(self.entity_type) < self.target_percent:
            free_cells = list(self.world.get_free_cells())
            if free_cells:
                x, y = choice(free_cells)
                self.world.add_entity(self.entity_type(x, y, self.speed_range, self.hp_range))
            # Генерация динамических объектов
