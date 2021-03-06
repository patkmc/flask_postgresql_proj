FROM python:3.10-buster

COPY requirements.txt requirements.txt

RUN pip --no-cache-dir install -r requirements.txt

COPY flask_app flask_app
COPY migrations migrations
COPY main.py main.py

EXPOSE 5000
