FROM ubuntu:latest
COPY ./challenge /home/caretaker

ARG USER=caretaker
ARG PASS=W1nj4_fl4g_0r_P4ssw0rd
ARG UID=1000
ARG GID=1000

RUN apt update -y && apt install -y make g++
RUN useradd -m ${USER} --uid=${UID} && echo "${USER}:${PASS}" | chpasswd

USER ${UID}:${GID}
WORKDIR /home/${USER}
