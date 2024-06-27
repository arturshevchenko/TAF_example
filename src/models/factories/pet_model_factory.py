from src.models.enums.pet_status_enum import PetStatus
from src.models.request.pet.pet_model import PetModel
from src.utils.data_generator import DataGenerator
from src.utils.enum_utils import EnumUtils


class PetModelFactory:

    @staticmethod
    def pet_only_required():
        return PetModel(
                name=DataGenerator.string_alphanumeric_of(20)
        )

    @staticmethod
    def pet_full():
        return PetModel(
                name=DataGenerator.string_alphanumeric_of(20),
                status=EnumUtils.get_random_value(PetStatus),
                photoUrls=[DataGenerator.string_alphanumeric_of(20)]
        )
