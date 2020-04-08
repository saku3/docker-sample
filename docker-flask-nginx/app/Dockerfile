FROM ubuntu
USER root

RUN mkdir /var/www

WORKDIR /var/www

RUN apt-get update && \
    apt-get -y install software-properties-common && \
    add-apt-repository -y ppa:deadsnakes && \
    apt-get update && \
    apt-get -y install nginx && \
    apt-get -y install python3.6-dev && \
    apt-get -y install python3-pip

RUN ln -s /usr/bin/python3.6 /usr/bin/python
RUN rm -rf /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3

RUN pip3 install --upgrade pip && pip install flask && pip install uwsgi

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]