from models import Entity
from models.predator import Predator


class PredatorTransformationService:
    '''
    Класс для трансформации объекта в Predator, если его HP достигает 100.
    '''

    def __init__(self, world, speed_of_predator, hp_of_predator):
        self.world = world
        self.speed_of_predator = speed_of_predator
        self.hp_of_predator = hp_of_predator

    def transform_to_predator(self, entity: Entity) -> None:
        """
        Трансформирует объект в Predator, если его HP достигает 100.
        Args:
            entity (Entity): Объект, который нужно трансформировать.
        """
        if entity.hp >= 100:
            predator = Predator(entity.x, entity.y, self.speed_of_predator, self.hp_of_predator)
            self.world.remove_entity(entity)
            self.world.add_entity(predator)
