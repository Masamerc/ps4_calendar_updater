from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
from tqdm import tqdm
from colorama import init, Fore
from bs4 import BeautifulSoup


def check_calendars(credentials):    
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

def scrape(data):
    """
    Scrape the data from metacritic.com, sotre it in a dictionary, and then append it to a list
    """
    url = 'https://www.metacritic.com/browse/games/release-date/coming-soon/ps4/date'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
        (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    games = soup.find_all("div", {"class":"product_wrap"})
    for game in games:
        title = game.find("div", {"class":"basic_stat product_title"})
        for tag in game.find_all("li", {"class":"stat release_date"}):
            release_date = tag.find("span", {"class":"data"})
        pair = {
            "title":title.text.strip(),
            "release_date":release_date.text.strip()
        }
        data.append(pair)


def save_credentials():
    """
    Save credentials required to access Google Calendar API and store them in a pickle file
    """
    scopes = ['https://www.googleapis.com/auth/calendar']
    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scopes=scopes)
    my_credentials = flow.run_console()
    return my_credentials
        

def update_calendar(data, calender_id, credentials):
    """
    Access Google Calendar API and create events with the name of upcoming PS4 game
    and its corresponding release date.
    """
    credentials = credentials
    service = build("calendar", "v3", credentials=credentials)
    # update calendar
    for datum in tqdm(data, desc="Updating Calendar", unit=" events"):
        user_calender_id = calender_id
        created_event = service.events().quickAdd(
            calendarId=user_calender_id,
            text=f'{datum["title"]} on {datum["release_date"]}').execute()


if __name__ == "__main__":
    credentials = save_credentials()
    check_calendars(credentials)
    YOUR_CALENDAR_ID = input("What's your calendar ID?: ")
    game_data = []
    print("Starting...", "\n")
    scrape(game_data)
    print("Data scraped from metacritic.com", "\n")
    update_calendar(game_data, YOUR_CALENDAR_ID, credentials)
    print(Fore.GREEN + "Calendar successfully updated")
    print("Happy Gaming!")