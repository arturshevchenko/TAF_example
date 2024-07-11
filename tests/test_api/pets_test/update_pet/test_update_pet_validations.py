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
@allure.feature("update pet")
@allure.title("update pet positive")
@pytest.mark.parametrize(
    "pet_model",
    [
        [
            PetModel(
                name=DataGenerator.string_alphanumeric_dash_dot_huphen(1),
            ),
            "all values from min boundary",
        ],
        [
            PetModel(
                name=DataGenerator.string_alphanumeric_dash_dot_huphen(255),
            ),
            "all values upper boundary",
        ],
    ],
)
def test_update_valid_boundary_pets(pets_factory, pet_model):
    # create pet
    pet = pets_factory()

    # prepare
    pet_model, _ = pet_model
    pet_model.id = pet.get("id")

    # send request
    response = PetsService().update_pet(pet=pet_model)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_OK_200))
    PetResponseBody(response=response).compare_with(pet_model)


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("update pet")
@allure.title("update pet negative boundaries")
@pytest.mark.parametrize(
    "pet_model",
    [
        [
            PetModel(name=DataGenerator.string_of(256)),
            "name",
            "validation_length_out_of_range",
        ]
    ],
)
def test_update_invalid_boundary_pets(pets_factory, pet_model):
    # create pet
    pet = pets_factory()

    # prepare
    pet_model, field, error = pet_model
    pet_model.id = pet.get("id")

    # send request
    response = PetsService().update_pet(pet=pet_model)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..field", equal_to(field)))
    response.should_have(body("$..description", equal_to(error)))


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("update pet")
@allure.title("update pet without required fields")
@pytest.mark.parametrize("pet_model", [[PetModel(), "name", "validation_required"]])
def test_update_without_required_fields_pets(pets_factory, pet_model):
    # create pet
    pet = pets_factory()

    # prepare
    pet_model, field, error = pet_model
    pet_model.id = pet.get("id")

    # send request
    response = PetsService().update_pet(pet=pet_model)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..field", equal_to(field)))
    response.should_have(body("$..description", equal_to(error)))


@pytest.mark.regression
@pytest.mark.negative
@allure.feature("update pet")
@allure.title("update pet invalid fields")
@pytest.mark.parametrize(
    "pet_model",
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
def test_update_invalid_fields_pets(pets_factory, pet_model):
    # create pet
    pet = pets_factory()

    # prepare
    pet_model, field, error = pet_model
    pet_model.id = pet.get("id")

    # send request
    response = PetsService().update_pet(pet=pet_model)

    # check status code and body
    response.should_have(status_code(StatusCode.HTTP_BAD_REQUEST_400))
    response.should_have(body("$..field", equal_to(field)))
    response.should_have(body("$..description", equal_to(error)))
