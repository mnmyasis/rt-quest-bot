from django.core.exceptions import ObjectDoesNotExist
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)

from . import controllers
from .apps import logger
from .models import Slug, Menu
from . import exceptions


class Routes:
    """Маршрутизация запопросов."""
    COMMAND_ROUTES = (
        ('start', controllers.start),
        ('test', controllers.test),
        ('inline', controllers.inline),
    )

    CONTROLLERS = {
        'main': controllers.command,
        'chat': controllers.chat
    }

    def __init__(self, updater: Updater):
        self.updater = updater

    def check_menu_type(self, type_menu: str) -> controllers:
        """Проверка типа меню. Возвращает контроллер."""
        controller = self.CONTROLLERS.get(type_menu)
        if not controller:
            raise exceptions.NotDocumentedBotController(
                f'Незадокументированный контроллер для типа меню: {type_menu}'
            )
        return controller

    def check_path(self, path: str) -> str:
        """Проверка пути. Возвращает slug."""
        try:
            slug = Slug.objects.get(value=path)
        except ObjectDoesNotExist:
            raise exceptions.BotPathNotFound(f'{path} NOT FOUND')
        return slug.value

    def check_menu(self, slug: str) -> str:
        """Проверка соотвествуия слага и меню."""
        try:
            menu = Menu.objects.get(slug__value=slug)
        except ObjectDoesNotExist:
            raise exceptions.BotMenuNotFound(
                f'Нет меню со слагом: {slug}'
            )
        return menu.type_menu

    def message_routes(self, update, context) -> None:
        """Маршрутизация по сообщению."""
        logger.debug((f'path: {update.message.text} '
                      f'chat_id: {update.message.chat_id} '
                      f'user: {update.message.from_user} '
                      ))
        try:
            slug = self.check_path(update.message.text)
            type_menu = self.check_menu(slug)
            controller = self.check_menu_type(type_menu)
            controller(update, context, slug)
        except exceptions.BotMenuNotFound as error:
            logger.error(error)
        except exceptions.BotPathNotFound as  error:
            logger.error(error)
        except exceptions.NotDocumentedBotController as error:
            logger.error(error)
        else:
            logger.info('Сообщение успешно отправлено.')

    def initial_command_routes(self) -> None:
        """Инициализация маршрутов команд."""
        for command_route in self.COMMAND_ROUTES:
            logger.debug(f'command route initial: {command_route}')
            route, controller = command_route
            self.updater.dispatcher.add_handler(
                CommandHandler(route, controller)
            )

    def initial_messages_routes(self) -> None:
        self.updater.dispatcher.add_handler(
            MessageHandler(Filters.text, self.message_routes)
        )

    def initial(self) -> None:
        """Инициализация всех маршрутов."""
        self.initial_command_routes()
        self.initial_messages_routes()
