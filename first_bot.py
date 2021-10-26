from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import BOT_TOKEN


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Soy un bot!"
    )

start_handler = CommandHandler('start', start)


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=update.message.text
    )


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)


if __name__ == "__main__":
    updater = Updater(token=BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
