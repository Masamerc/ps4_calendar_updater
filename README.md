# ps4_release_calendar

## 1. Overview 
A web-scraping project which updatates your Goolge Calendar with release dates of upcoming PS4 games.

The main goal is to help PS4 gamers like myself who have no time or too lazy to go to websites like IGN to check upcoming PS4 games.
<br>
<br>

**Script in action**

![script in action](./images/in_action.png)

**Updated Calndar**

![updated calendar](./images/updated_calendar.png)
<br>
<br>
## 2. Instructions

### Goolge Calendar API
To access your Google calendar using Python you need to set up Google Calendar API. 
This [Youtube tutorial](https://www.youtube.com/watch?v=j1mh0or2CX8&list=PL4vwZmJNbv_Mr2jbVwOuLlqYdS1dyXWKs&index=15) by Indian Pythonista explains the process very well. (watch it until the initial setup.)

If you have wathched tutotorial, you should have credentials you need saved as ```client_secrets.json```.
Place the file in the main project directory and in the ```pickle/``` folder.

<br>

### Installing Dependencies
All the packages/modules required can be found in ```requirements.txt```
To install, simply use pip:

```pip install -r /path/to/requirements.txt```

<br>

### Running the Script

There are two ways to run the script: with or without pickle. 

***without pickle***

*every time you run any of the scripts, you will be prompted to login to your Google Account to authorize the app


First, run the ```check_calendar.py```, which prints out the name and id of each Google calendar you have (I recommend you create a new calendar just for the release dates so you can toggle it on/off), and take note of the id of calendar you want to use for the script. 

Alternatively, you can just log in to your Google calendar and click "configure" on the calendar you want to use, and then scroll down to find the id. 

Paste the id in the ```update_calendar``` function found at the bottom of ```main_scraper.py``` as the third argument, and run the ```main_scraper.py``` script.

<br>

***with pickle🥒***

*with pickle that stores you credentials, you will only be prompted once to log in to your Google account

First run the ```save_creds.py``` which will prompt you to log in and authorize the app, and then stores credentials as ```token.pkl```.

Then run the ```check_calendar_pickle.py```, which prints out the name and id of each Google calendar you have, and take note of the id of calendar you want to use for the script. 

Paste the id in the ```update_calendar``` function found at the bottom of ```scraper_pickle.py``` as the third argument, and run the ```scraper_pickle.py``` script.
