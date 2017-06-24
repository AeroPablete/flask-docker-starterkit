FROM python:3.5
MAINTAINER Pablo Oñate <pablo.onate.villaverde@gmail.com>

ENV INSTALL_PATH /usr/src/app
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# COPY . .
VOLUME $INSTALL_PATH