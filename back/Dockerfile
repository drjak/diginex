FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app/app.py /app

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
