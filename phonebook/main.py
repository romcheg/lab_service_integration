from flask import Flask, request
from record import Record

app = Flask(__name__)


phonebook = {
    1: Record(
        first_name="John",
        last_name="Doe"
        phone_number="9379992",
        country="Poland",
    ),
    2: Record(
        first_name="Jane",
        last_name="Doe",
        phone_number="223322223322",
        country="Ukraine",
    ),
}


@app.get("/records/")
def list_records():
    return [phonebook[record_id].to_json() for record_id in phonebook], 200


@app.get("/records/<int:record_id>")
def get_one_record(record_id):
    if record_id not in phonebook:
        return {"message": "Not found"}, 404

    return phonebook[record_id].to_json()


app.run(host="0.0.0.0", port=8080)
