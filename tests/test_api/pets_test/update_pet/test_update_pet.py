import allure
import pytest
from hamcrest import equal_to

from src.assert_steps.strategies.pet_response_compare import PetResponseBody
from src.configs.status_code import StatusCode
from src.models.factories.pet_model_factory import PetModelFactory
from src.services.http_client.conditions import status_code, body
from src.services.services.pets_service import PetsService
from src.utils.data_generator import DataGenerator


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("update pet")
@allure.title("update pet positive")
@pytest.mark.parametrize(
    "pet_model", [PetModelFactory.pet_full(), PetModelFactory.pet_only_required()]
)
def test_update_valid_pet(pets_factory, pet_model):
    # prepare
    pet = pets_factory(PetModelFactory.pet_full())

    pet_model_updated = PetModelFactory.pet_full()
    pet_model_updated.id = pet.get("id")

    # send request
    response = PetsService().update_pet(pet=pet_model_updated)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))
    PetResponseBody(response=response).compare_with(pet_model_updated)


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("update pet")
@allure.title("update pet not found")
def test_update_not_found_id_pet():
    pet_model_new = PetModelFactory.pet_full()
    pet_model_new.id = DataGenerator.random_int(10000000, 99999999)
    # send request
    response = PetsService().update_pet(pet=pet_model_new)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))
    PetResponseBody(response=response).compare_with(pet_model_new)


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("update pet")
@allure.title("update pet invalid id")
def test_update_invalid_id_pet():
    pet_model_new = PetModelFactory.pet_full()
    pet_model_new.id = DataGenerator.string_of(5)

    # send request
    response = PetsService().update_pet(pet=pet_model_new)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..status", equal_to("InvalidArgument")))
    response.should_have(body("$..field", equal_to("pet_id")))
