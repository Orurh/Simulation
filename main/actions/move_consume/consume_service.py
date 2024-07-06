from actions.Pathfinding import PathfindingService
from actions.init_actions import DynamicEntityGeneratorStrategy
from config.settings import speed_of_predator, hp_of_predator
from models import Entity, Herbivore
from models.predator import Predator


class ConsumptionService(PathfindingService):
    def __init__(self, world):
        self.world = world

    def move_to(self, entity: Entity, x: int, y: int) -> None:
        """
        Перемещает объект на новую позицию и обновляет его положение и hp на карте
        Args:
            entity (Entity): Объект, который нужно переместить.
            x (int): Новая координата X.
            y (int): Новая координата Y.
        """
        # Удаляем объект из его текущей позиции
        self.world.remove_entity(entity)
        if entity.hp == 0:
            return
        # Обновляем координаты объекта
        entity.x = x
        entity.y = y
        # проверяем класс объекта и изменяем его hp
        if not isinstance(entity, Herbivore):
            entity.hp -= 10
        # Добавляем объект на новую позицию
        self.world.add_entity(entity)


    def consume_target(self, entity: Entity, target: Entity) -> None:
        """
        Уничтожает целевой объект и обновляет состояние карты.

        Args:
            entity (Entity): Объект, который поедает цель.
            target (Entity): Объект, который нужно съесть.
        """

        # Удаляем объект-цель с карты
        self.world.remove_entity(target)
        if entity.hp >=100:
            predator = Predator(entity.x, entity.y, speed_of_predator, hp_of_predator)
            self.move_to(predator, target.x, target.y)
            return
        # Перемещаем объект на место, где была цель
        self.move_to(entity, target.x, target.y)
        entity.hp += 10