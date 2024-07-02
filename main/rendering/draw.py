from config.settings import width, height

def draw_map(world):
    for y in range(height):
        for x in range(width):
            if world.get_entity_at(x, y) is None:
                print("|__|", end="")
            else:
                print(world.get_entity_at(x, y), end="")

        print()

