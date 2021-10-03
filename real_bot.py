import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from local_settings import BOT_TOKEN
from quotes import QUOTES


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Soy un bot que dice frases bonitas"
    )

start_handler = CommandHandler('start', start)


def send_quotes(update, context):
    user_message = update.message.text
    matching_quotes = [
        quote for quote in QUOTES if user_message in quote
    ]
    if not matching_quotes:
        matching_quotes = QUOTES

    selected_quote = random.choice(matching_quotes)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=selected_quote
    )


quotes_handler = MessageHandler(Filters.text & (~Filters.command), send_quotes)


if __name__ == "__main__":
    updater = Updater(token=BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(quotes_handler)

    updater.start_polling()
