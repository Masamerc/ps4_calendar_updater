from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import json

credentials = pickle.load(file=open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

calendar_items = service.calendarList().list().execute()

calendars = []

for item in calendar_items["items"]:
    entry = {}
    print(f"Calendar Name: {item['summary']}")
    entry["Calendar Name"] = item["summary"]
    print(f"Calendar ID: {item['id']}")
    entry["ID"] = item["id"]
    print("\n")
    calendars.append(entry)

with open("calendars.json", "w") as f:
    json.dump(calendars, f, indent=2)

print("Your calendar data has been saved to \"calendars.json\" ")
