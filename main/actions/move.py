import random

from actions.move_action import MoveAction
from models import Entity


class Move(MoveAction):
    def generate(self, target_percent) -> None:
        pass

    def move_to(self, entity: Entity, x: int, y: int) -> None:
        """
        Перемещает объект на новую позицию и обновляет его положение на карте.

        Args:
            entity (Entity): Объект, который нужно переместить.
            x (int): Новая координата X.
            y (int): Новая координата Y.
        """
        # Удаляем объект из его текущей позиции
        self.world.remove_entity(entity)

        # Обновляем координаты объекта
        entity.x = x
        entity.y = y

        # Добавляем объект на новую позицию
        self.world.add_entity(entity)

    def consume_target(self, entity: Entity, target: Entity) -> None:
        """
        Уничтожает целевой объект и обновляет состояние карты.

        Args:
            entity (Entity): Объект, который поедает цель.
            target (Entity): Объект, который нужно съесть.
        """
        # Перемещаем объект на место, где была цель
        self.move_to(entity, target.x, target.y)

        # Удаляем объект-цель с карты
        self.world.remove_entity(target)

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
        path = self.bfs_path(entity, goal_type)
        if path:
            next_step = path[1]
            print(next_step, path)
            # print(path, path[-1][0], path[-1][1])
            if next_step == (path[-1][0], path[-1][1]):
                # Если следующий шаг - это конечная ячейка, съедаем объект
                target = self.world.get_entity_at(path[-1][0], path[-1][1])
                print(target)
                if target and target.type == goal_type:
                    self.consume_target(entity, target)
                    return True
            self.move_to(entity, next_step[0], next_step[1])
            return True
        else:
            # Если не удалось найти путь, даем объекту случайное перемещение
            self.random_move(entity)
            return False

    def random_move(self, entity: Entity) -> None:
        """
        Перемещает объект в случайную свободную клетку.

        Args:
            entity (Entity): Объект, который нужно переместить.
        """
        free_cells = self.world.get_free_cells()
        if free_cells:
            random_cell = random.choice(free_cells)
            self.move_to(entity, random_cell[0], random_cell[1])
