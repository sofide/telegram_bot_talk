import os


SITE_DOMAIN = 'https://sofi-talk-bot.herokuapp.com'
DEBUG = True

# google_sheet settings
FEEDBACK_SPREADSHEET_NAME = "Telegram feedback"
FEEDBACK_WORKSHEET_INDEX = 0  # first tab or sheet inside the spreadsheet

# Google Drive credentials
DRIVE_FILE_KEY = "sheet_client_key.json"
if not DRIVE_FILE_KEY in os.listdir():
    _client_key = os.environ["DRIVE_CLIENT_KEY"]
    with open(DRIVE_FILE_KEY, "w") as key_file:
        key_file.write(_client_key)

# Heroku settings
if os.environ.get('HEROKU', False):
    BOT_TOKEN = os.environ.get('BOT_TOKEN')
    DEBUG = False
else:
    from local_settings import BOT_TOKEN
