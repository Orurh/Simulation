import asyncio
import os
import sys

from actions.init_actions import StaticEntityGeneratorStrategy, DynamicEntityGeneratorStrategy
from actions.move_consume.movent_service import Move
from config.config import GameConfig
from models import Herbivore, Rock, Tree
from models.grass import Grass
from models.predator import Predator
from rendering.draw import draw_map


class SimulationManager:
    def __init__(self, world, game_config: GameConfig):
        self.game_config = game_config
        self.world = world(game_config.height, game_config.width)
        self.entity_generators = [
            StaticEntityGeneratorStrategy(self.world, Rock, game_config.persent_of_rock),
            StaticEntityGeneratorStrategy(self.world, Tree, game_config.persent_of_tree),
            DynamicEntityGeneratorStrategy(self.world, Grass, game_config.persent_of_grass, game_config.speed_of_grass,
                                           game_config.hp_of_grass),
            DynamicEntityGeneratorStrategy(self.world, Herbivore, game_config.persent_of_herbivore,
                                           game_config.speed_of_herbivore, game_config.hp_of_herbivore),
        ]
        self.turn_count = 0
        self.is_running = False

    async def start_simulation(self) -> None:
        self.is_running = True
        while self.is_running:
            await self.next_turn()

    def pause_simulation(self) -> None:
        self.is_running = False

    async def next_turn(self) -> None:
        self.turn_count += 1
        for generator in self.entity_generators:
            generator.generate_or_perform_action()

        herbs = self.world.get_entities_of_type(Herbivore)
        preds = self.world.get_entities_of_type(Predator)

        for _ in range(min(self.game_config.speed_of_herbivore, self.game_config.speed_of_predator)):
            for herb in herbs:
                Move(self.world).move(herb, Grass)
            for pred in preds:
                Move(self.world).move(pred, Herbivore)
            self.render_world()
            await asyncio.sleep(0.1)
            self.clear_console()

        # Выполняем дополнительные ходы для Predator, если его скорость больше
        if self.game_config.speed_of_predator > self.game_config.speed_of_herbivore:
            for _ in range(self.game_config.speed_of_predator - self.game_config.speed_of_herbivore):
                for pred in preds:
                    Move(self.world).move(pred, Herbivore)
                self.render_world()
                await asyncio.sleep(0.1)
                self.clear_console()

        self.render_world()
        await asyncio.sleep(0.2)
        self.clear_console()

    def render_world(self) -> None:
        draw_map(self.world, self.game_config.height, self.game_config.width)
        print(f"Turn: {self.turn_count}")

    def clear_console(self) -> None:
        """Очищает консоль в зависимости от операционной системы"""
        # Проверяем, на какой ОС запускается скрипт
        if sys.platform.startswith('win'):
            os.system('cls')  # Для Windows
        else:
            os.system('clear')  # Для Unix-подобных ОС (Linux, macOS)
