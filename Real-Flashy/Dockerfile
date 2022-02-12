FROM rhub/debian-gcc11

ARG USER=caretaker
ARG PASS=W1nj4_fl4g_0r_P4ssw0rd
ARG UID=1000
ARG GID=1000

RUN apt update -y --allow-releaseinfo-change 
RUN apt install -y make gcc openssh-server

RUN useradd -s /bin/bash -m ${USER} --uid=${UID} && echo "${USER}:${PASS}" | chpasswd
COPY ./challenge/ /home/${USER}/Real_Flashy/
COPY ./flag.txt /root/flag.txt
WORKDIR /home/${USER}/Real_Flashy/

RUN make 
RUN mv ./cxxmatrix /usr/bin/screensaver
RUN chmod +s /usr/bin/screensaver

ENTRYPOINT service ssh start;bash

