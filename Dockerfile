FROM python:3.8-buster 

WORKDIR /opt/app

COPY requirements.lock /opt/app
COPY MicroRCA_Online/MicroRCA_online.py /opt/app
RUN pip3 install -r requirements.lock
