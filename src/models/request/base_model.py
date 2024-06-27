import json


class BaseModel:

    def return_body(self) -> dict:
        return json.loads(self.json_string())

    def json_string(self) -> str:
        return json.dumps(self, default=lambda e: e.__dict__)

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_dict(cls, adict):
        pass
