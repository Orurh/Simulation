import random

from actions.Pathfinding import PathfindingService
from actions.move_consume.consume_service import ConsumptionService
from models import Entity, Herbivore

class Move(ConsumptionService):
    def generate_or_perform_action(self, entity: Entity) -> None:
        """
        Перемещает объект на 1 шаг в случайном направлении.
        Args:
            entity (Entity): Объект, который нужно переместить.
        """
        # Список возможных направлений
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Выбираем случайное направление
        dx, dy = random.choice(directions)

        # Определяем новые координаты
        new_x = entity.x + dx
        new_y = entity.y + dy

        # Проверяем, что новая позиция находится в пределах карты и не занята
        if 0 <= new_x < self.world.width and 0 <= new_y < self.world.height and not self.world.is_blocked(new_x, new_y):
            self.move_to(entity, new_x, new_y)
        else:
            # Если новая позиция недоступна, остаемся на месте
            pass



    def move(self, entity: Entity, goal_type: type) -> bool:
        """
        Перемещает данный объект к ближайшей свободной клетке, ведущей к ближайшему объекту заданного типа.
        Если объект достигает ячейки, где находится цель, то он съедает ее.

        Args:
            entity (Entity): Объект, который необходимо переместить.
            goal_type (type): Тип объекта, к которому нужно двигаться.

        Returns:
            bool: True, если движение было успешным, False - в противном случае.
        """
        path = self.a_star_path(entity, goal_type)
        if path:
            next_step = path[1]
            if next_step == (path[-1][0], path[-1][1]):
                # Если следующий шаг - это конечная ячейка, съедаем объект
                target = self.world.get_entity_at(path[-1][0], path[-1][1])
                if target and type(target) == goal_type:
                    self.consume_target(entity, target)
                    return True
            self.move_to(entity, next_step[0], next_step[1])
            return True
        else:
            # Если не удалось найти путь, даем объекту случайное перемещение
            self.generate_or_perform_action(entity)
            return False
