from abc import ABC, abstractmethod


class EntityGeneratorStrategy(ABC):
    def __init__(self, world):
        self.world = world

    @abstractmethod
    def generate_or_perform_action(self, entity_type, target_percent) -> None:
        pass
