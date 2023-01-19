import json

from flask import Flask, request
import pika

app = Flask(__name__)

@app.post("/greeting/")
def send_greeting():
    """
    {
        "name": "Kateryna",
        "message": "bla bla bla"
    }
    """
    greeting_task = request.json

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="127.0.0.1",
            port=56721,
            credentials=pika.PlainCredentials(
                username="admin",
                password="admin"
            )
        )
    )
    channel = connection.channel()
    channel.basic_publish(exchange="", routing_key="tasks", body=json.dumps(greeting_task))





    return {"message": "sent successfully"}, 200


app.run(host="0.0.0.0", port=8100)
