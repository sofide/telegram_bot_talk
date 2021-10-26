from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from settings import DRIVE_FILE_KEY


# Google API Credentials
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
creds = ServiceAccountCredentials.from_json_keyfile_name(DRIVE_FILE_KEY, scope)
client = gspread.authorize(creds)

FEEDBACK_SHEET_NAME = "Telegram feedback"
FEEDBACK_SHEET = client.open(FEEDBACK_SHEET_NAME).sheet1


def add_feedback(feedback, username, full_name):
    now_date = datetime.now()
    now_str = datetime.strftime(now_date, "%d/%m/%y %H:%M:%S")
    FEEDBACK_SHEET.append_row([now_str, username, full_name, feedback])
