FROM python:latest

WORKDIR /user/src/app
COPY . /user/src/app

RUN pip install -r requirements.txt