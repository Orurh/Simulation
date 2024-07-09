from actions.move_consume.consume_service import ConsumptionService
from actions.move_consume.movent_service import Move
from actions.not_working_files_for_the_future.init_predators import PredatorTransformationService
from config.config import GameConfig


class ServiceProvider:
    '''
    Заготовка класса инициализации передачи параметров в класс Move например, выделеие логики создания объектов по
    изменяемым параметрам HP и скорости
    '''

    def __init__(self, world, game_config: GameConfig):
        self.world = world
        self.game_config = game_config
        self.predator_transformation_service = PredatorTransformationService(self.world,
                                                                             self.game_config.speed_of_predator,
                                                                             self.game_config.hp_of_predator)
        self.consumption_service = ConsumptionService(self.world, self.predator_transformation_service,
                                                      self.entity_creation_service)
        self.move_service = Move(self.world, self.consumption_service)
