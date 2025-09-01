# integrations/google_sheets.py
import gspread
from google.oauth2.service_account import Credentials
import os
from datetime import datetime

# স্কোপ
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def get_sheet_client(sheet_name="TripGenie_Requests"):
    """Google Sheets এ কানেক্ট করুন"""
    creds_path = os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH", "secrets/gsheets-creds.json")
    
    credentials = Credentials.from_service_account_file(creds_path, scopes=SCOPES)
    client = gspread.authorize(credentials)
    
    try:
        sheet = client.open(sheet_name).sheet1
        return sheet
    except Exception as e:
        print(f"❌ Sheet not found: {e}")
        return None

def log_trip_request(city, days, preferences, feedback=None):
    """
    Google Sheets-এ ট্রিপ রিকোয়েস্ট লগ করুন
    """
    sheet = get_sheet_client()
    if not sheet:
        return False

    try:
        sheet.append_row([
            city,
            days,
            preferences,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            feedback or ""
        ])
        print("✅ Trip request logged to Google Sheets")
        return True
    except Exception as e:
        print(f"❌ Failed to log to Google Sheets: {e}")
        return False

# টেস্ট
if __name__ == "__main__":
    log_trip_request("Paris", 3, "food, museums", "positive")
