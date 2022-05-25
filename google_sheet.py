from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from settings import DRIVE_FILE_KEY, FEEDBACK_SPREADSHEET_NAME, FEEDBACK_WORKSHEET_INDEX


# Google API Credentials
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
]
creds = ServiceAccountCredentials.from_json_keyfile_name(DRIVE_FILE_KEY, scope)
client = gspread.authorize(creds)

feedback_spreadsheet = client.open(FEEDBACK_SPREADSHEET_NAME)
feedback_sheet = feedback_spreadsheet.get_worksheet(FEEDBACK_WORKSHEET_INDEX)


def add_feedback(feedback, username, full_name):
    now_date = datetime.now()
    now_str = datetime.strftime(now_date, "%d/%m/%y %H:%M:%S")
    feedback_sheet.append_row([now_str, username, full_name, feedback])
