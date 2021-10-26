import os

SITE_DOMAIN = 'https://sofi-talk-bot.herokuapp.com'
DEBUG = True

# Heroku settings
if os.environ.get('HEROKU', False):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    DEBUG = False
else:
    from local_settings import BOT_TOKEN
