import json
import time

import pika


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

while True:
    tasks = channel.consume("tasks", auto_ack=True)

    for task in tasks:
        _, _, message = task

        greeting = json.loads(message)
        print(f"Hello {greeting['name']}! You have a greeting message: {greeting['message']}.")

    time.sleep(10)
