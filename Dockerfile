FROM python:3.7
ENV PYTHONUNBUFFERED 1
MAINTAINER the-vladman
ADD . /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate