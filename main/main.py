from actions.action import EntityGeneratorStrategy
from actions.init_actions import StaticEntityGeneratorStrategy, DynamicEntityGeneratorStrategy
from config.settings import *
from models.grass import Grass
from models.tree import Tree
from simulation.map import Map
from rendering.draw import draw_map
from models.rock import Rock
from models.herbivore import Herbivore
from actions.move_action import MoveAction


class SimulationManager:
    def __init__(self, strategy: EntityGeneratorStrategy):
        self.strategy = strategy

    def execute(self) -> None:
        self.strategy.generate()

    # Использование


if __name__ == '__main__':
    world = Map(height, width)
    entity_generators = [
        SimulationManager(StaticEntityGeneratorStrategy(world, Rock, persent_of_rock)),
        SimulationManager(StaticEntityGeneratorStrategy(world, Tree, persent_of_tree)),
        SimulationManager(StaticEntityGeneratorStrategy(world, Grass, persent_of_grass)),
        SimulationManager(
            DynamicEntityGeneratorStrategy(world, Herbivore, persent_of_herbivore, hp_of_herbivore, speed_of_herbivore))
    ]

for generator in entity_generators:
    generator.execute()

draw_map(world)
herbs = world.get_entities_of_type(Herbivore)
print(herbs[0].x, herbs[0].y)
