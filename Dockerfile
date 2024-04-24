# syntax=docker/dockerfile:1

FROM python:3.9

RUN mkdir /app
ADD . /app/
WORKDIR /app/


RUN pip install -r requirements.txt

ENV DEBUG=False
