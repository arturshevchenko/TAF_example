import pytest

from src.configs.config_loader import AppConfigs
from src.configs.status_code import StatusCode
from src.models.factories.pet_model_factory import PetModelFactory
from src.models.request.pet.pet_model import PetModel
from src.services.http_client.conditions import status_code
from src.services.services.pets_service import PetsService


@pytest.fixture(name="pets_factory")
def pets_factory():
    pets = []

    # create pet
    def create_pet(pet_model: PetModel = None) -> dict:
        # prepare model
        if pet_model is None:
            pet_model = PetModelFactory.pet_full()
        # create pet
        pet_created_json = PetsService().create_pet(pet=pet_model).get_json()
        pets.append(pet_created_json)
        return pet_created_json

    # do tests
    yield create_pet

    # delete pet
    if AppConfigs.CLEAR_DATA:
        for pet in pets:
            # delete pet after test
            PetsService().delete_pet(pet_id=pet.get("id"))


@pytest.fixture(name="pet_deleter")
def pet_deleter():
    def _delete_pet(pet_id):
        (
            PetsService()
            .delete_pet(pet_id=pet_id)
            .should_have(status_code(StatusCode.HTTP_OK_200))
        )

    return _delete_pet
