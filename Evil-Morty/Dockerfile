FROM ubuntu:latest

ARG USER=flask
ARG PASS=flask
ARG UID=1000
ARG GID=1000

RUN apt update -y
RUN apt install -y python3 python3-pip
RUN pip3 install uwsgi
RUN pip3 install flask

RUN useradd -s /usr/sbin/nologin -m ${USER} --uid=${UID} && echo "${USER}:${PASS}" | chpasswd
COPY ./templates/ /home/${USER}/templates/
COPY ./app.py /home/${USER}/app.py
COPY ./flag.txt /flag.txt
WORKDIR /home/${USER}/

ENTRYPOINT uwsgi --plugins http,python3 --http 0.0.0.0:8000 --module app:app --processes 1 --threads 20 --wsgi-file /home/${USER}/app.py
USER ${UID}:${GID}

