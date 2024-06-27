import allure
import pytest

from src.configs.status_code import StatusCode
from src.services.http_client.conditions import status_code
from src.services.services.pets_service import PetsService


@pytest.mark.smoke
@pytest.mark.positive
@allure.feature('get pets')
@allure.title("get pets without qury params ")
def test_get_valid_pets():
    # send request
    response = PetsService().get_pets()

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_NOT_ALLOWED_405))
