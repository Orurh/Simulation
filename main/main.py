import os
import sys
from time import sleep


from actions.action import EntityGeneratorStrategy
from actions.init_actions import StaticEntityGeneratorStrategy, DynamicEntityGeneratorStrategy
from actions.move_consume.movent_service import Move
from config.settings import *
from models import Herbivore
from models.grass import Grass
from models.predator import Predator
from models.rock import Rock
from models.tree import Tree
from rendering.draw import draw_map
from simulation.map import Map

class SimulationManager:
    def __init__(self, strategy: EntityGeneratorStrategy):
        self.strategy = strategy

    def execute(self) -> None:
        self.strategy.generate_or_perform_action()

    # Использование


if __name__ == '__main__':
    world = Map(height, width)
    entity_generators = [
        SimulationManager(StaticEntityGeneratorStrategy(world, Rock, persent_of_rock)),
        SimulationManager(StaticEntityGeneratorStrategy(world, Tree, persent_of_tree)),
        SimulationManager(StaticEntityGeneratorStrategy(world, Grass, persent_of_grass)),
        SimulationManager(
            DynamicEntityGeneratorStrategy(world, Herbivore, persent_of_herbivore, speed_of_herbivore, hp_of_herbivore)),
    ]

for generator in entity_generators:
    generator.execute()

def clear_console():
    """Очищает консоль в зависимости от операционной системы"""
    # Проверяем, на какой ОС запускается скрипт
    if sys.platform.startswith('win'):
        os.system('cls')  # Для Windows
    else:
        os.system('clear')  # Для Unix-подобных ОС (Linux, macOS)


herbs = world.get_entities_of_type(Herbivore)
grasses = world.get_entities_of_type(Grass)

# print(herbs[0].hp)

for x in range(90):
    try:
        # Получаем список всех Herbivore и Predator в мире
        herbs = world.get_entities_of_type(Herbivore)
        preds = world.get_entities_of_type(Predator)

        # Перемещаем всех Predator
        for pred in preds:
            # Сначала проверяем, есть ли в мире Herbivore
            if world.get_entities_of_type(Herbivore):
                Move(world).move(pred, Herbivore)
            else:
                # Если Herbivore нет, перемещаем Predator к ближайшей Grass
                Move(world).move(pred, Grass)

        # Перемещаем всех Herbivore, но только каждые 2 итерации
        if x % 2 == 0:
            for herb in herbs:
                Move(world).move(herb, Grass)

    except Exception as e:
        pass

    draw_map(world)
    sleep(0.2)
    clear_console()
    # print(herbs[0].hp)




# if path:
#     print(f"Path found: {path}")
# else:
#     print("Path not found")