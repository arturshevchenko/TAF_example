import allure
import pytest

from src.assert_steps.strategies.pet_response_compare import PetResponseBody
from src.configs.status_code import StatusCode
from src.models.factories.pet_model_factory import PetModelFactory
from src.services.http_client.conditions import status_code
from src.services.services.pets_service import PetsService


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature('create pet')
@allure.title("create pet positive")
@pytest.mark.parametrize("pet", [
        PetModelFactory.pet_full(),
        PetModelFactory.pet_only_required(),
])
def test_create_valid_pet(pet):
    # send request
    response = PetsService() \
        .create_pet(pet=pet)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))
    PetResponseBody(response=response).compare_with(pet)

    # delete pet after test
    PetsService() \
        .delete_pet(pet_id=response.get_json().get('id')) \
        .should_have(status_code(StatusCode.HTTP_OK_200))
