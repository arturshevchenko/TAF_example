import allure
import pytest
from hamcrest import equal_to

from src.assert_steps.strategies.pet_response_compare import PetResponseBody
from src.configs.status_code import StatusCode
from src.models.request.pet.pet_model import PetModel
from src.services.http_client.conditions import status_code, body
from src.services.services.pets_service import PetsService
from src.utils.data_generator import DataGenerator


@pytest.mark.regression
@pytest.mark.positive
@allure.feature("create pet")
@allure.title("create pet positive")
@pytest.mark.parametrize(
    "pet",
    [
        [
            PetModel(
                name=DataGenerator.string_of(1),
            ),
            "all values from min boundary",
        ],
        [
            PetModel(
                name=DataGenerator.string_of(255),
            ),
            "all values upper boundary",
        ],
    ],
)
def test_create_valid_boundary_pets(pet, pet_deleter):
    # prepare
    pet, _ = pet
    # send request
    response = PetsService().create_pet(pet=pet)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))
    PetResponseBody(response=response).compare_with(pet)

    # delete pet after test
    pet_id = response.get_json().get("id")
    pet_deleter(pet_id)


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("create pet")
@allure.title("create pet negative boundaries")
@pytest.mark.parametrize(
    "pet",
    [
        [
            PetModel(name=DataGenerator.string_of(256)),
            "name",
            "validation_length_out_of_range",
        ]
    ],
)
def test_create_invalid_boundary_pets(pet):
    # prepare
    pet, field, error = pet

    # send request
    response = PetsService().create_pet(pet=pet)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..field", equal_to(field)))
    response.should_have(body("$..description", equal_to(error)))


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("create pet")
@allure.title("create pet without required fields")
@pytest.mark.parametrize("pet", [[PetModel(), "name", "validation_required"]])
def test_create_without_required_fields_pets(pet):
    # prepare
    pet, field, error = pet

    # send request
    response = PetsService().create_pet(pet=pet)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..field", equal_to(field)))
    response.should_have(body("$..description", equal_to(error)))


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("create pet")
@allure.title("create pet invalid fields")
@pytest.mark.parametrize(
    "pet",
    [
        [
            PetModel(
                photoUrls=DataGenerator.string_alphanumeric_dash_dot_huphen(20),
            ),
            "photoUrls",
            "validation_is_list",
        ]
    ],
)
def test_create_invalid_fields_pets(pet):
    # prepare
    pet, field, error = pet

    # send request
    response = PetsService().create_pet(pet=pet)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..field", equal_to(field)))
    response.should_have(body("$..description", equal_to(error)))
