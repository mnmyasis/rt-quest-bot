from django.core.management.base import BaseCommand

from bot.main import start


class Command(BaseCommand):
    help = 'Запуск телеграм бота'

    def handle(self, *args, **options):
        start()
