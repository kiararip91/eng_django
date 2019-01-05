from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import random

# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/spreadsheets'
]

# The ID and range of the spreadsheet.
SPREADSHEET_ID = '1fO7gSpf-UtURwq86BUVsbWXvSZaIzHtM9scjLxaGAHU'
LAST_WORD_ROW = 233


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
    parsedWord = Word(english=row[0], italian=row[1], sentence=row[2], type=row[3], importance=row[4], right=0, error=0)
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

    # TODO: Renderlo relativo
    store = file.Storage('/Users/chiararipanti/Desktop/Python/djangoProjects/eng_django/eng_app/static/eng_app/token.json')
    creds = store.get()

    if not creds or creds.invalid:
        # TODO: Renderlo relativo
        flow = client.flow_from_clientsecrets('/Users/chiararipanti/Desktop/Python/djangoProjects/eng_django/eng_app/static/eng_app/client_secret.json', SCOPES)
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
