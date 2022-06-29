from telegram import Bot
from django.conf import settings

bot = Bot(settings.TELEGRAM_TOKEN)


def test(update, context):
    chat = update.effective_chat
    bot.send_message(chat.id, text='test message')

