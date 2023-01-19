from dataclasses import dataclass, asdict


@dataclass
class Record:
    first_name: str
    last_name: str
    phone_number: str
    country: str

    def to_json(self):
        return asdict(self)

    @classmethod
    def from_json(cls, data):
        return Record(**data)
