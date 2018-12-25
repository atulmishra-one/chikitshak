# Dockerfile
FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /srv/chikitshak
WORKDIR /srv/chikitshak
ADD requirements.txt /srv/chikitshak/
RUN pip install -r requirements.txt

ADD . /srv/

