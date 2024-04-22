# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

RUN apt update -y && apt install vim -y

RUN mkdir /app
ADD . /app/
WORKDIR /app/


RUN pip3 install -r requirements.txt

ENV DEBUG=False
