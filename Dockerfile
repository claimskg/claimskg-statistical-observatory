FROM ubuntu:19.04

MAINTAINER Andon Tchechmedjiev "andon.tchechmedjiev@mines-ales.fr"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install waitress

COPY . /app
RUN chmod +x /app/regenerate_dataframes.py
RUN ln -s /usr/bin/python3.7 /usr/bin/python


CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "8080"]
