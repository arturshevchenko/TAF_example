import time
from dataclasses import asdict
from typing import Dict

import allure

from src.configs.api_method import ApiMethod
from src.configs.config_loader import AppConfigs
from src.configs.endpoint import Endpoint
from src.models.request.pet.pet_model import PetModel
from src.services.http_client.response import AssertableResponse
from src.services.services.base_service import BaseService
from src.services.services.decorators import service_logger


class PetsService(BaseService):

    def __init__(self, session=None):
        super().__init__(session)
        if AppConfigs.THROTLING:
            time.sleep(0.1)

    @allure.step("create pet {pet}")
    @service_logger
    def create_pet(self, pet: PetModel) -> AssertableResponse:
        self._request \
            .set_path(Endpoint.PETS.value) \
            .set_method(ApiMethod.POST) \
            .set_body(asdict(pet))
        return AssertableResponse(self._request.send())

    @allure.step("get pet by id {pet_id}")
    @service_logger
    def get_pet_id(self, pet_id) -> AssertableResponse:
        self._request \
            .set_path(Endpoint.PET_ID.value.format(pet_id=pet_id)) \
            .set_method(ApiMethod.GET)
        return AssertableResponse(self._request.send())

    @allure.step("update pet by id {pet}")
    @service_logger
    def update_pet(self, pet: PetModel | Dict) -> AssertableResponse:
        if type(pet) is PetModel:
            pet = asdict(pet)

        self._request \
            .set_path(Endpoint.PETS.value) \
            .set_method(ApiMethod.PUT) \
            .set_body(pet)
        return AssertableResponse(self._request.send())

    @allure.step("delete pet {pet_id}")
    @service_logger
    def delete_pet(self, pet_id) -> AssertableResponse:
        self._request \
            .set_path(Endpoint.PET_ID.value.format(pet_id=pet_id)) \
            .set_method(ApiMethod.DELETE)
        return AssertableResponse(self._request.send())

    @allure.step("get pets")
    @service_logger
    def get_pets(self) -> AssertableResponse:
        self._request \
            .set_path(Endpoint.PETS.value) \
            .set_method(ApiMethod.GET)
        return AssertableResponse(self._request.send())

    @allure.step("FindByStatus pets")
    @service_logger
    def find_by_status(self, status=None) -> AssertableResponse:
        self._request \
            .set_path(Endpoint.PET_FIND_BY_STATUS.value) \
            .set_method(ApiMethod.GET) \
            .set_query_params(**{'status': status})
        return AssertableResponse(self._request.send())
