FROM ubuntu:latest

WORKDIR /usr/app/
COPY . .
RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask

CMD ["python3", "app.py"]