# Dockerfile
FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get -y -qq install gdal-bin binutils libproj-dev libgdal-dev
RUN mkdir -p /srv/chikitshak
WORKDIR /srv/chikitshak
ADD requirements.txt /srv/chikitshak/
RUN pip install -r requirements.txt

ADD . /srv/

