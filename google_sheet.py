import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


#Authorize the API
scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
key_filename = 'sheet_client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(key_filename, scope)
client = gspread.authorize(creds)

FEEDBACK_SHEET_NAME = "Telegram feedback"
FEEDBACK_SHEET = client.open(FEEDBACK_SHEET_NAME).sheet1


def add_feedback(feedback):
    FEEDBACK_SHEET.append_row([feedback])

