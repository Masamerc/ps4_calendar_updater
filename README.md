# ps4_release_calendar

## 1. Overview 
A web-scraping project which updatates your Goolge Calendar with release dates of upcoming PS4 games.
The main goal is to help PS4 gamers like myself who have no time or too lazy to go to websites just to check upcoming PS4 releases.

You can use docker to run the program as well. [Run with Docker](#Run-with-Docker🐋)
<br>

The project itself is a collection of python scripts which:
- Scrape game titles and release dates
- Connect to your calendar via Google Calendar API
- Update your calendar, addding release dates to your calendar. 
<br>

**Script in action**

![script in action](./images/in_action.png)

**Updated Calndar**

![updated calendar](./images/updated_calendar.png)
<br>
<br>
## 2. Uasge Instructions

### Goolge Calendar API
To access your Google Calendar using Python you need to set up Google Calendar API. 
This [Youtube tutorial](https://www.youtube.com/watch?v=j1mh0or2CX8&list=PL4vwZmJNbv_Mr2jbVwOuLlqYdS1dyXWKs&index=15) by Indian Pythonista explains the process very well. (watch it until the initial setup.)

If you have wathched tutotorial, you should have required credentials saved as ```client_secrets.json```.
Save it the file in the main project directory along with python scripts. 

---
### Installing Dependencies

All the packages/modules required can be found in ```requirements.txt```
To install, simply run the following command in the project directory:

```pip install -r requirements.txt```

Packages installed in this project's environment are:
```
beautifulsoup4
google-api-python-client
google-auth
google-auth-httplib2
google-auth-oauthlib
httplib2
oauthlib
requests
requests-oauthlib
rsa
six
soupsieve
tqdm
uritemplate
urllib3
colorama
```
---
### Running the Script
with pickle that stores you credentials, you will only be prompted once to log in to your Google account

1. First run the ```save_creds.py``` which will prompt you to log in and authorize the app, and store credentials as ```token.pkl```.

```
$ python save_creds.py
```

*please make sure the ```client_secrets.json``` file is saved in the same directory as well.*

2. (optional) Run the ```check_calendar.py```, which prints out the name and id of each Google calendar you have and save them to a json file for later reference, and take note of the id of calendar you want to use for the script. Alternatively you can go to your calendar on Goolge Calendar and check the id in settings.
```
$ python check_calendar.py
```

3. Run the ```update_calendar.py``` and paste your calendar id when promted.
```
$ python update_calendar.py

What's your calendar ID?: 
``` 

<br>

---

### Run with Docker🐋

1. Build a docker container with the supplied Dockerfile. You can name the container whatever you want. 

```docker
# Dockerfile

FROM python:latest

COPY . /user/src/app
WORKDIR /user/src/app

RUN pip install -r requirements.txt

CMD python docker_update.py
```

```
$ docker build . -t CONTAINER_NAME
```

2. Run the container like so: (make sure you use the "-it" tag since it requires interactivity for authentication)
```
$ docker run -it CONTAINER_NAME
```
