FROM python:latest

COPY . /user/src/app
WORKDIR /user/src/app

RUN pip install -r requirements.txt

CMD python docker_update.py