import asyncio

from config.config import GameConfig
from simulation.map import Map
from simulation.simulation import SimulationManager

if __name__ == '__main__':
    game_config = GameConfig()
    simulation_manager = SimulationManager(Map, game_config)
    asyncio.run(simulation_manager.start_simulation())
