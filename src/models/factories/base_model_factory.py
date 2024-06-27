from src.models.request.base_model import BaseModel


class BaseModelFactory:

    @staticmethod
    def only_required():
        return BaseModel(

        )
