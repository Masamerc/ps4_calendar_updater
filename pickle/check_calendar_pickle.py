from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

credentials = pickle.load(file=open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

calendar_items = service.calendarList().list().execute()

for item in calendar_items["items"]:
    print(f"Calendar Name: {item['summary']}")
    print(f"Calendar ID: {item['id']}")
    print("\n")
    
