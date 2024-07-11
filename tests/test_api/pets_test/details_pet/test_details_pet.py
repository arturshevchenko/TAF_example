import allure
import pytest
from hamcrest import equal_to, contains_string

from src.assert_steps.strategies.pet_response_compare import PetResponseBody
from src.configs.status_code import StatusCode
from src.models.factories.pet_model_factory import PetModelFactory
from src.services.http_client.conditions import status_code, body
from src.services.services.pets_service import PetsService
from src.utils.data_generator import DataGenerator


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature("get pet details")
@allure.title("get pet details positive")
@pytest.mark.parametrize(
    "pet_model", [PetModelFactory.pet_full(), PetModelFactory.pet_only_required()]
)
def test_get_valid_pet_details(pets_factory, pet_model):
    # prepare
    pet = pets_factory(pet_model)

    # send request
    response = PetsService().get_pet_id(pet_id=pet.get("id"))

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))
    PetResponseBody(response=response).compare_with(pet_model)


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("get pet details")
@allure.title("get pet details not found")
def test_get_not_found_id_pet():
    # send request
    response = PetsService().get_pet_id(pet_id=DataGenerator.random_uuid4())

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_NOT_FOUND_404))
    response.should_have(body("$..code", equal_to(404)))
    response.should_have(body("$..type", equal_to("unknown")))
    response.should_have(
        body("$..message", contains_string("java.lang.NumberFormatException"))
    )


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("get pet details")
@allure.title("get pet details invalid id")
def test_get_invalid_id_pet():
    # send request
    response = PetsService().get_pet_id(pet_id=DataGenerator.string_of(5))

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_NOT_FOUND_404))
    response.should_have(body("$..code", equal_to(404)))
    response.should_have(body("$..type", equal_to("unknown")))
    response.should_have(
        body("$..message", contains_string("java.lang.NumberFormatException"))
    )
