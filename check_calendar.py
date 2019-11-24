from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from main_scraper import save_credentials

scopes = ['https://www.googleapis.com/auth/calendar']

credentials = save_credentials()

service = build("calendar", "v3", credentials=credentials)

calendar_items = service.calendarList().list().execute()

for item in calendar_items["items"]:
    print(f"Calendar Name: {item['summary']}")
    print(f"Calendar ID: {item['id']}")
    print("\n")
    