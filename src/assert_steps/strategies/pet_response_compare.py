from dataclasses import asdict

from hamcrest import equal_to, not_

from src.services.http_client.conditions import body
from src.services.http_client.response import AssertableResponse


class PetResponseBody:

    def __init__(self, response: AssertableResponse):
        self._response = response

    def compare_with(self, pet):
        if type(pet) is not dict:
            pet_to_compare = asdict(pet)
        else:
            pet_to_compare = pet

        self._response.should_have(body("$..id", not_(None)))
        self._response.should_have(body("$..name", equal_to(pet_to_compare.get('name'))))
        self._response.should_have(body("$..tags", equal_to([])))

        if pet_to_compare.get('status') is not None:
            self._response.should_have(body("$..status", equal_to(pet_to_compare.get('status'))))
        if pet_to_compare.get('photoUrls') is not None:
            self._response.should_have(body("$..photoUrls", equal_to(pet_to_compare.get('photoUrls'))))
