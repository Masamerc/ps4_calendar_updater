from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from bs4 import BeautifulSoup
import requests
import pickle
from tqdm import tqdm
from colorama import init, Fore

init()

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
    pickle.dump(my_credentials, file=open("token.pkl", "wb"))
        

def update_calendar(data, calender_id):
    """
    Access Google Calendar API and create events with the name of upcoming PS4 game
    and its corresponding release date.
    """
    credentials = pickle.load(file=open("token.pkl", "rb"))
    service = build("calendar", "v3", credentials=credentials)
    # update calendar
    for datum in tqdm(data, desc="Updating Calendar", unit=" events"):
        user_calender_id = calender_id
        created_event = service.events().quickAdd(
            calendarId=user_calender_id,
            text=f'{datum["title"]} on {datum["release_date"]}').execute()


if __name__ == "__main__":
    YOUR_CALENDAR_ID = input("What's your calendar ID?: ")
    game_data = []
    print("Starting...", "\n")
    scrape(game_data)
    print("Data scraped from metacritic.com", "\n")
    update_calendar(game_data, YOUR_CALENDAR_ID)
    print(Fore.GREEN + "Calendar successfully updated")
    print("Happy Gaming!")
