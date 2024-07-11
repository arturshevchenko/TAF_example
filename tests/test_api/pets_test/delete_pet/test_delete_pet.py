import allure
import hamcrest
import pytest
from hamcrest import equal_to, contains_string

from src.configs.status_code import StatusCode
from src.models.factories.pet_model_factory import PetModelFactory
from src.services.http_client.conditions import status_code, body
from src.services.services.pets_service import PetsService
from src.utils.data_generator import DataGenerator


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("delete pet")
@allure.title("delete pet positive")
def test_delete_pet(pets_factory):
    # prepare
    pet = pets_factory(PetModelFactory.pet_full())

    # send request
    response = PetsService().delete_pet(pet_id=pet.get("id"))

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("delete pet")
@allure.title("delete pet not found")
def test_delete_not_found_id_pet():
    # send request
    response = PetsService().delete_pet(pet_id=DataGenerator.random_uuid4())

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_NOT_FOUND_404))
    response.should_have(body("$..code", equal_to(404)))
    response.should_have(body("$..type", equal_to("unknown")))
    response.should_have(
        body("$..message", contains_string("java.lang.NumberFormatException"))
    )


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("delete pet")
@allure.title("delete pet invalid id")
def test_delete_invalid_id_pet():
    # send request
    response = PetsService().delete_pet(pet_id=DataGenerator.string_of(5))

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_NOT_FOUND_404))
    response.should_have(body("$..code", equal_to(404)))
    response.should_have(body("$..type", equal_to("unknown")))
    response.should_have(
        body("$..message", contains_string("java.lang.NumberFormatException"))
    )
