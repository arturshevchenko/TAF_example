import json


class BaseDataClass:

    def without_nullable(self):
        dict_result = {}
        for key, value in self.__dict__.items():
            if value is not None:
                dict_result[key] = value
        return dict_result

    def get_body(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_dict(cls, adict):
        pass
