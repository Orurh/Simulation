from config.config import GameConfig


class GameContext:
    def __init__(self, world, game_config: GameConfig):
        self.world = world
        self.game_config = game_config
