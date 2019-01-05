from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import random
import os

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/spreadsheets'
]

TOKEN_RELATIVE_PATH = "static/eng_app/token.json"
CLIENT_SECRET_RELATIVE_PATH = "static/eng_app/client_secret.json"

# The ID and range of the spreadsheet.
SPREADSHEET_ID = '1fO7gSpf-UtURwq86BUVsbWXvSZaIzHtM9scjLxaGAHU'
LAST_WORD_ROW = 235


class Word:
    def __init__(self, english, italian, sentence, type, importance, right, error):
        self.english = english
        self.italian = italian
        self.sentence = sentence
        self.type = type
        self.importance = importance
        self.right = right
        self.error = error


def rowToWord(row):
    parsedWord = Word(english=row[1], italian=row[2], sentence=row[3], type=row[4], importance=row[5], right=0, error=0)
    return parsedWord


def updateCell(service, position, value):
    body = {
        "values":
        [
            [
                value
            ]
        ]
    }
    request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=position, valueInputOption="RAW", body=body)
    request.execute()


def getWord():

    randomIndex = random.randint(2, LAST_WORD_ROW)
    range = 'A' + str(randomIndex) + ':G' + str(randomIndex)

    store = file.Storage(os.path.dirname(os.path.abspath(__file__)) + "/" + TOKEN_RELATIVE_PATH)
    creds = store.get()

    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(os.path.dirname(os.path.abspath(__file__)) + "/" + CLIENT_SECRET_RELATIVE_PATH, SCOPES)
        creds = tools.run_flow(flow, store)

    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()

    values = result.get('values', [])
    parsedWord = rowToWord(values[0])
    word = {
        'english': parsedWord.english,
        'italian': parsedWord.italian,
        'sentence': parsedWord.sentence,
        'correct': parsedWord.right,
        'wrong': parsedWord.error}
    return word
