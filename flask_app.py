from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher

from real_bot import add_all_handlers
from settings import BOT_TOKEN, SITE_DOMAIN, DEBUG


app = Flask(__name__)
bot = Bot(BOT_TOKEN)

dispatcher = Dispatcher(bot, None)
add_all_handlers(dispatcher)

@app.route("/")
def index():
    return "Hello World!"


@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def bot_response():
    print("im in bot response!!")
    update = request.get_json()
    dispatcher.process_update(Update.de_json(update, bot))

    print("im in bot response!! - before return")
    return {"ok": True}


@app.route("/test")
def test():
    return "Hello Sofi!"


@app.route("/webhook")
def send_set_webhook():
    webhook_endpoint = f"{SITE_DOMAIN}/{BOT_TOKEN}"
    print("about to sed webhook")
    print("endpoint:", webhook_endpoint)
    bot.set_webhook(webhook_endpoint)
    return "webhook ready"
