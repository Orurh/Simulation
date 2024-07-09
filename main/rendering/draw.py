from models import Herbivore


def draw_map(world, height, width):
    for y in range(height):
        for x in range(width):
            if world.get_entity_at(x, y) is None:
                print("|__|", end="")
            else:
                print(world.get_entity_at(x, y), end="")
        print()

    print('====' * width)
    sas = world.get_entities_of_type(Herbivore)
    print(sas[0], len(sas))
    print()
