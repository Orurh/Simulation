from typing import Dict, Tuple, List, Optional, Set
from models.entity import Entity


class Map:
    def __init__(self, width: int, height: int):
        """
        Инициализирует объект карты.

        :param width: Ширина карты
        :param height: Высота карты
        """
        self.width = width
        self.height = height
        self.entities: Dict[Tuple[int, int], Entity] = {}  # Словарь для хранения всех объектов на карте
        self.free_cells: List[Tuple[int, int]] = [(x, y) for x in range(width) for y in
                                                  range(height)]  # Инициализация всех свободных ячеек

    def add_entity(self, entity: Entity) -> None:
        """
        Добавляет новый объект на карту.

        :param entity: Объект, который нужно добавить
        :raises ValueError: Если ячейка, в которую нужно добавить объект, уже занята
        """
        key = (entity.x, entity.y)
        if key in self.entities:
            raise ValueError("Cannot add entity to occupied cell")
        self.entities[key] = entity
        self.free_cells.remove(key)

    def remove_entity(self, entity: Entity) -> None:
        """
        Удаляет объект с карты.

        :param entity: Объект, который нужно удалить
        """
        key = (entity.x, entity.y)
        del self.entities[key]
        self.free_cells.append(key)

    def get_entity_at(self, x: int, y: int) -> Optional[Entity]:
        """
        Получает объект, находящийся в указанной координате.

        :param x: Координата X
        :param y: Координата Y
        :return: Если в указанной ячейке есть объект, то возвращает его, иначе возвращает None
        """
        key = (x, y)
        return self.entities.get(key, None)


    def get_free_cells(self) -> List[Tuple[int, int]]:
        """
        Получает список всех свободных ячеек на карте.

        :return: Список свободных ячеек
        """
        return self.free_cells[:]

    def get_occupied_cells(self) -> Set[Tuple[int, int]]:
        """
        Получает множество всех занятых ячеек на карте.

        :return: Множество занятых ячеек
        """
        return set(self.entities.keys())

    def get_percent_occupied(self) -> float:
        """
        Получает процент занятых ячеек на карте.

        :return: Процент занятых ячеек
        """
        return (len(self.entities) / (self.width * self.height)) * 100


    def get_entities_of_type(self, entity_type: type) -> List[Entity]:
        """
        Получает список всех объектов на карте указанного типа.

        :param entity_type: Тип объектов, которые нужно получить
        :return: Список объектов указанного типа
        """
        return [entity for entity in self.entities.values() if isinstance(entity, entity_type)]

    def get_count_of_type(self, entity_type: type) -> int:
        """
        Получает количество объектов на карте указанного типа.

        :param entity_type: Тип объектов, которые нужно подсчитать
        :return: Количество объектов указанного типа
        """
        return len(self.get_entities_of_type(entity_type))

    def get_percent_of_type(self, entity_type: type) -> float:
        """
        Получает процент объектов на карте указанного типа.
        :param entity_type: Тип объектов, для которых нужно получить процент
        :return: Процент объектов указанного типа
        """
        count_of_type = self.get_count_of_type(entity_type)
        return (count_of_type / (self.width * self.height)) * 100
