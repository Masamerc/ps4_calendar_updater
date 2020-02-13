from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

# uncomment the line below to use the file in the main directory (MAC/LINUX)
CLIENT_SECRETS_FILE = "./client_secrets.json"

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=scopes)
credentials = flow.run_console()


pickle.dump(credentials, file=open("token.pkl", "wb"))
