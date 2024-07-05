from collections import deque
from math import sqrt
from typing import Optional, Tuple, List
from actions.action import EntityGeneratorStrategy
from models.entity import Entity



class MoveAction(EntityGeneratorStrategy):
    def init(self, world):
        self.world = world

    def find_nearest_food(self, entity: Entity, food):
        foods = self.world.get_entities_of_type(food)
        if foods:
            nearest_food = min(foods, key=lambda e: abs(e.x - entity.x) + abs(e.y - entity.y))
            nearest_cell = self.find_nearest_free_cell(nearest_food)
            return nearest_cell, (nearest_food.x, nearest_food.y)
        return None

    def find_nearest_free_cell(self, entity: Entity) -> Optional[Tuple[int, int]]:
        closest_distance = float('inf')
        closest_cell = None

        for x, y in self.world.get_free_cells():
            distance = sqrt((x - entity.x) ** 2 + (y - entity.y) ** 2)
            if distance < closest_distance:
                closest_distance = distance
                closest_cell = (x, y)

        return closest_cell

    def bfs_path(self, entity: Entity, food) -> Optional[List[Tuple[int, int]]]:
        start_pos = (entity.x, entity.y)
        goal, last_step = self.find_nearest_food(entity, food)
        # last_step = (last_step.x, last_step.y)

        if goal is None:
            return None

        free_cells = self.world.get_free_cells()
        queue = deque([(start_pos, [start_pos])])
        visited = set([start_pos])

        while queue:
            current_pos, path = queue.popleft()
            if current_pos == goal:
                path.append(last_step)
                if entity.current_path != path:
                    entity.current_path = path
                    return path
            for neighbor in [(current_pos[0] - 1, current_pos[1]),
                             (current_pos[0] + 1, current_pos[1]),
                             (current_pos[0], current_pos[1] - 1),
                             (current_pos[0], current_pos[1] + 1)]:
                if (neighbor in free_cells
                        and neighbor not in visited):
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def generate(self, target_percent) -> None:
        pass
