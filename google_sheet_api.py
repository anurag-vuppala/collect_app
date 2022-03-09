from curses import raw
import sqlite3
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json
import sqlalchemy
from numpy import insert



    

def update_data_to_sheet():
    
    sheet_name = 'spotify'
    DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
    engine = sqlalchemy.create_engine(DATABASE_LOCATION)
    conn = sqlite3.connect('my_played_tracks.sqlite')
    cur = conn.cursor()
    data = cur.execute("select * from my_played_tracks").fetchall()
    
    key = 'sheet_creds.json'
    scope = ['https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive.readonly',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/spreadsheets.readonly',
                ]

    creds = None
    creds = service_account.Credentials.from_service_account_file(key,scopes=scope)
    sheetid = '1bdPEicAieaus4AWU92_Ry11f4XMiYJSncJiWh42bd28'
    service = build('sheets','v4',credentials=creds)
    sheet = service.spreadsheets()
    ranges = sheet_name + '!A2' 
    update_data = sheet.values().update(spreadsheetId=sheetid, range=ranges,valueInputOption='USER_ENTERED', body = {"values": data}).execute()
    return update_data





# key = 'sheet_creds.json'
# scope = ['https://www.googleapis.com/auth/drive',
#          'https://www.googleapis.com/auth/drive.file',
#          'https://www.googleapis.com/auth/drive.readonly',
#          'https://www.googleapis.com/auth/spreadsheets',
#          'https://www.googleapis.com/auth/spreadsheets.readonly',
#             ]

# creds = None
# creds = service_account.Credentials.from_service_account_file(key,scopes=scope)
# sheetid = '1bdPEicAieaus4AWU92_Ry11f4XMiYJSncJiWh42bd28'
# service = build('sheets','v4',credentials=creds)
# sheet = service.spreadsheets()
# this is to get the values from the sheet
# result = sheet.values().get(spreadsheetId=sheetid, range="sheet1!A1:C5").execute()


# # this is to update values in the sheet

# # input_value = [[1,"anurag", "vuppala"],[2,"anushike","biskit"]]

# # result = sheet.values().update(spreadsheetId=sheetid, range="sheet1!A1", valueInputOption='USER_ENTERED', body = {"values": input_value}).execute()
# print(result)

########################

#to append values to sheet , will add data at the end of the list

# append_data = [[3,"venkataswaramma","vuppla"]]


# etoro, amazon , insta , twitter, spotify , amazon music , apple music, youtube, 

#####################



print(update_data_to_sheet())
    



