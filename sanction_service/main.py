from flask import Flask, request
import requests


app = Flask(__name__)

@app.get("/sanctioned-clients/")
def get_sanctioned_clients():
    """
    {
       "parameter_name": "string"
       "parameter_value": "any"
    }

    Example:
    {
       "parameter_name: "first_name"
       "parameter_value": "Tetiana"
    }
    """

    phonebook_service_endpoint = "http://127.0.0.1:8080/records/"
    response = requests.get(phonebook_service_endpoint)

    clients = response.json()

    criterias = request.json

    sanctioned_clients = []
    sanction_parameter = criterias["parameter_name"]
    sanction_value = criterias["parameter_value"]

    for client in clients:
        if client[sanction_parameter] == sanction_value:
            sanctioned_clients.append(client)

    return sanctioned_clients, 200


app.run(host="0.0.0.0", port=8090)
