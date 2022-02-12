FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
RUN apt update -y && apt install -y php

COPY ./ /var/www/html/
WORKDIR /var/www/html/

ENTRYPOINT php -S 0.0.0.0:8080 
USER www-data:www-data

### run
# docker build -t magician:latest .
# docker run -itdp 8080:8080 --name magician magician:latest bash
