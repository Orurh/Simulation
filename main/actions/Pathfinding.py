from heapq import heappop, heappush
from math import sqrt
from typing import Optional, Tuple, List
from actions.action import EntityGeneratorStrategy
from models.entity import Entity


class PathfindingService(EntityGeneratorStrategy):
    """
    Стратегия для определения движения сущностей на карте.
    Реализует алгоритм A* для нахождения кратчайшего пути между двумя ячейками.
    """

    def find_nearest_food(self, entity: Entity, food) -> Optional[Tuple[int, int]]:
        """
        Находит ближайшую еду заданного типа к указанной сущности.
        Args:
            entity (Entity): объект, для которого ищется ближайшая еда.
            food_type (Type[Entity]): Тип еды, которую нужно найти.
        Returns:
            Optional[Tuple[int, int]]: Координаты ближайшей еды или `None`, если еда не найдена.
        """
        foods = self.world.get_entities_of_type(food)
        if foods:
            nearest_food = min(foods, key=lambda e: abs(e.x - entity.x) + abs(e.y - entity.y))
            return nearest_food.x, nearest_food.y
        return None

    def heuristic(self, a: Tuple[int, int], b: Tuple[int, int]) -> float:
        """Эвристическая функция, оценивающая расстояние между двумя ячейками"""
        (x1, y1) = a
        (x2, y2) = b
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def a_star_path(self, entity: Entity, food_type) -> Optional[List[Tuple[int, int]]]:
        """
        Находит кратчайший путь между двумя ячейками с помощью алгоритма A*
        Returns:
            Список координат ячеек, образующих кратчайший путь, или `None`, если путь не найден.

        """

        start = (entity.x, entity.y)
        goal = self.find_nearest_food(entity, food_type)
        if goal is None:
            return None
        frontier = [(0, start, [start])]
        visited = set()
        while frontier:
            _, current_pos, path = heappop(frontier)
            if current_pos == goal:
                return path
            if current_pos in visited:
                continue
            visited.add(current_pos)

            for neighbor in self.get_neighbors(current_pos, goal):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    heappush(frontier, (len(new_path) + self.heuristic(neighbor, goal), neighbor, new_path))

        return None

    def get_neighbors(self, pos: Tuple[int, int], goal: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Возвращает список доступных соседних ячеек для заданной позиции"""
        x, y = pos
        neighbors = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        valid_neighbors = []
        for nx, ny in neighbors:
            if (nx, ny) == goal or (
                    0 <= nx < self.world.width and 0 <= ny < self.world.height and not self.world.is_blocked(nx, ny)):
                valid_neighbors.append((nx, ny))

        return valid_neighbors

    def generate_or_perform_action(self, target_percent) -> None:
        """
        Метод для генерации новых сущностей на карте.
        Этот метод не используется в классе MoveAction, но наследуется от абстрактного класса EntityGeneratorStrategy.
        Куда прикрутить пока не придумал.
        """
        pass
