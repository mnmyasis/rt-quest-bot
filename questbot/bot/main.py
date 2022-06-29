from telegram import Bot
from django.conf import settings

bot = Bot(settings.TELEGRAM_TOKEN)
TELEGRAM_ADMIN_ID = settings.TELEGRAM_ADMIN_ID


def send_message(message):
    bot.send_message(TELEGRAM_ADMIN_ID, text=message)


def start():
    print('bot is started')


if __name__ == '__main__':
    send_message('test')
