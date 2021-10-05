import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from google_sheet import add_feedback
from local_settings import BOT_TOKEN
from quotes import (
    ALL_QUOTES,
    HARRY_POTTER_QUOTES,
    LORD_OF_THE_RINGS_QUOTES,
    STAR_WARS_QUOTES,
)


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Soy un bot que dice frases bonitas."
    )

start_handler = CommandHandler('start', start)


def send_quotes(update, context):
    user_message = update.message.text
    matching_quotes = [
        quote for quote in ALL_QUOTES if user_message in quote
    ]
    if not matching_quotes:
        matching_quotes = ALL_QUOTES

    selected_quote = random.choice(matching_quotes)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=selected_quote
    )

quotes_handler = MessageHandler(Filters.text & (~Filters.command), send_quotes)


def harry_potter_quotes(update, context):
    user_message = ' '.join(context.args)
    matching_quotes = [
        quote for quote in HARRY_POTTER_QUOTES if user_message in quote
    ]
    if not matching_quotes:
        matching_quotes = HARRY_POTTER_QUOTES

    selected_quote = random.choice(matching_quotes)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=selected_quote
    )

harry_potter_handler = CommandHandler('hp', harry_potter_quotes)


def quotes_of(quotes_list):
    def quotes_command(update, context):
        user_message = ' '.join(context.args)
        matching_quotes = [
            quote for quote in quotes_list if user_message in quote
        ]
        if not matching_quotes:
            matching_quotes = quotes_list

        selected_quote = random.choice(matching_quotes)

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=selected_quote
        )

    return quotes_command

lord_of_the_rings_handler = CommandHandler('lotr', quotes_of(LORD_OF_THE_RINGS_QUOTES))
star_wars_handler = CommandHandler('sw', quotes_of(STAR_WARS_QUOTES))


def feedback(update, context):
    feedback_text = ' '.join(context.args)
    username = getattr(update.message.from_user, "username", "")
    full_name = getattr(update.message.from_user, "full_name", "")

    add_feedback(feedback_text, username, full_name)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Gracias por tu feedback!"
    )

feedback_handler = CommandHandler('feedback', feedback)

def anonymous_feedback(update, context):
    feedback_text = ' '.join(context.args)

    add_feedback(feedback_text, "-", "-")

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Gracias por tu feedback anónimo!"
    )

anonymous_feedback_handler = CommandHandler('feedack_anonimo', anonymous_feedback)

if __name__ == "__main__":
    updater = Updater(token=BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(quotes_handler)
    dispatcher.add_handler(harry_potter_handler)
    dispatcher.add_handler(lord_of_the_rings_handler)
    dispatcher.add_handler(star_wars_handler)
    dispatcher.add_handler(feedback_handler)
    dispatcher.add_handler(anonymous_feedback_handler)

    updater.start_polling()
