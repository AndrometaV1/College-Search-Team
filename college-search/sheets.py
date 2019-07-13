import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("CollegeInfo").sheet1  # Opens the spreadsheet


def row():
    # Get a specific row
    print(sheet.row_values(int(input("What row would you like to see?: "))))


def col():
    print(sheet.row_values(int(input("What column would you like to see?: "))))


def cell():
    print(sheet.row_values(int(input("What cell would you like to see?: "))))


numRows = sheet.row_count  # Get the number of rows in the sheet

college = sheet.row_values(1)

# if sheet.row_values(1)

# access_dictionary()
