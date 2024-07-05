from actions.action import EntityGeneratorStrategy
from actions.init_actions import StaticEntityGeneratorStrategy, DynamicEntityGeneratorStrategy
from actions.move import Move
from config.settings import *
from models import Herbivore
from models.grass import Grass
from models.tree import Tree
from simulation.map import Map
from rendering.draw import draw_map
from models.rock import Rock
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
print()
herbs = world.get_entities_of_type(Herbivore)
grasses = world.get_entities_of_type(Grass)

Move(world).move(herbs[0], Grass)
draw_map(world)
print()
Move(world).move(herbs[0], Grass)
draw_map(world)
print()
Move(world).move(herbs[0], Grass)
draw_map(world)
print()
Move(world).move(herbs[0], Grass)
draw_map(world)
print()
# for grass in grasses:
#     print(grass.x, grass.y)
# print(MoveAction(world).find_nearest_food(herbs[0], Grass).x, MoveAction(world).find_nearest_food(herbs[0]).y, Grass)
# x = MoveAction(world).find_nearest_food(herbs[0], Grass)
# for herb in herbs:
#     path=MoveAction(world).a_star_path(herb, Grass)
#     print(path)


# if path:
#     print(f"Path found: {path}")
# else:
#     print("Path not found")