#create a docker file for Currency Converter to run on a container
FROM python:3.7.3

RUN mkdir -p /usr/src/app

RUN apt-get update -y\
    && apt-get -y install python3-pip 

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]

