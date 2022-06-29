from telegram.ext import Updater, CommandHandler

from . import controllers
from .apps import logger


class Routes:
    """Маршрутизация запопросов."""
    command_routes = (
        ('test', controllers.test),
    )

    def __init__(self, updater: Updater):
        self.updater = updater

    def initial_command_routes(self):
        """Инициализация маршрутов команд."""
        for command_route in self.command_routes:
            logger.debug(f'command route initial: {command_route}')
            route, controller = command_route
            self.updater.dispatcher.add_handler(
                CommandHandler(route, controller)
            )

    def initial(self):
        """Инициализация всех маршрутов."""
        self.initial_command_routes()
