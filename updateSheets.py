from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def update_values(data1, data2, data3, data4, data5):
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    key = "creds.json"
    creds = service_account.Credentials.from_service_account_file(filename=key, scopes=scopes)

    try:
        spreadsheet_id = "1ar--YOUR SPREADSHEET ID--p0"
        range_name = "A2:E2"
        value_input_option = "USER_ENTERED"
        service = build("sheets", "v4", credentials=creds)
        values = [[
            data1,
            data2,
            data3,
            data4,
            data5,
        ], ]
        body = {"values": values}
        result = (
            service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption=value_input_option,
                body=body,
            )
            .execute()
        )
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
