import logging
import sys

from django.apps import AppConfig


class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(levelname)s - %(asctime)s - %(message)s'
)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)
