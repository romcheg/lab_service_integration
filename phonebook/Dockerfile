FROM docker.io/python:3.10-alpine

ADD ./ /app
RUN pip3 install -r /app/requirements.txt

ENTRYPOINT [ "python3", "/app/main.py" ]
