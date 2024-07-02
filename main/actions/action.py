from abc import ABC, abstractmethod

class EntityGeneratorStrategy(ABC):
    def __init__(self, world, entity_type, target_percent):
        self.world = world
        self.entity_type = entity_type
        self.target_percent = target_percent
    @abstractmethod
    def generate(self, entity_type, target_percent) -> None:
        pass