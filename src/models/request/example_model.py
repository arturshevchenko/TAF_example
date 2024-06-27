import json

from src.models.request.base_model import BaseModel


class ExampleModel(BaseModel):

    def __str__(self):
        return f"example: {self.return_body()}"

    def __repr__(self):
        return f"example: \n\t{self.return_body()}"

    def __init__(self, field: str = None):
        self.req = dict()

        if field is not None:
            self.req['field'] = self._field = field

    @property
    def field(self):
        return self._field

    def json_string(self):
        return json.dumps(self.req, default=lambda e: e.__dict__)
