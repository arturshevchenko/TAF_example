import allure
import hamcrest
import pytest

from src.configs.status_code import StatusCode
from src.models.enums.pet_status_enum import PetStatus
from src.models.factories.pet_model_factory import PetModelFactory
from src.services.http_client.conditions import status_code, body
from src.services.services.pets_service import PetsService
from src.utils.data_generator import DataGenerator


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("search pets")
@allure.title("search pets by status")
@pytest.mark.parametrize(
    "status",
    [
        PetStatus.AVAILABLE.value,
        PetStatus.SOLD.value,
        PetStatus.PENDING.value,
    ],
)
def test_search_pet_by_status(pets_factory, status):
    pet1_model = PetModelFactory.pet_full()
    pet1_model.status = status

    # create review pet
    pets_factory(pet1_model)

    # search pet
    pets = PetsService().find_by_status(
        status=status,
    )
    pets.should_have(status_code(StatusCode.HTTP_OK_200))
    pets.should_contain(body("$..status", hamcrest.only_contains(status)))


@pytest.mark.regression
@pytest.mark.positive
@allure.feature("search pets")
@allure.title("search pets by status not found")
def test_search_pet_by_status_not_found():
    # save review pet
    status = DataGenerator.string_of(100)

    # search pet
    pets = PetsService().find_by_status(status=status)
    pets.should_have(status_code(StatusCode.HTTP_OK_200))
