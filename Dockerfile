FROM ubuntu:19.04

MAINTAINER Andon Tchechmedjiev "andon.tchechmedjiev@mines-ales.fr"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev gunicorn3 redis

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt
RUN pip3 install waitress redis

COPY . /app
RUN chmod +x /app/regenerate_dataframes.py
RUN chmod +x /app/run-server.sh
#RUN ln -s /usr/bin/python3.7 /usr/bin/python


CMD [ "/app/run-server.sh"]
