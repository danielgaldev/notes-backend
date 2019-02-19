FROM python:3.7-alpine
RUN apk update && apk add postgresql-dev musl-dev gcc
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
