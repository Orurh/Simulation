from actions.action import EntityGeneratorStrategy

class MoveAction(EntityGeneratorStrategy):
    def __init__(self, world, entity_type, target_percent = None):
        self.world = world
        self.entity_type = entity_type
        self.target_percent = target_percent

    def move_entity(self, entity, new_x, new_y):
        self.world.move_entity(entity, new_x, new_y)

    def generate(self, entity_type, target_percent) -> None:
        pass