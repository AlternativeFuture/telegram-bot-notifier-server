# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt update -y && apt install vim -y
COPY . .

ENV DEBUG=False

#CMD gunicorn -w 4 -t 360000 -b :5001 'app:app'


#FROM python:3.9-slim
#
## Установка зависимостей
#RUN pip install flask psycopg2-binary python-telegram-bot
#
## Копирование файлов приложения в контейнер
#COPY ./app /app
#
## Указание рабочей директории
#WORKDIR /app

# Команда для запуска сервера
CMD ["python", "server.py"]