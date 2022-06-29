from telegram.ext import Updater
from django.conf import settings

from .routes import Routes
from .apps import logger

TELEGRAM_ADMIN_ID = settings.TELEGRAM_ADMIN_ID
updater = Updater(settings.TELEGRAM_TOKEN)


def start():
    logger.info('Bot is started')
    routes = Routes(updater)
    routes.initial()
    updater.start_polling()
    updater.idle()
