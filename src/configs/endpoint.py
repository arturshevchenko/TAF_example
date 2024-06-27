from enum import Enum


class Endpoint(Enum):
    """
    All kind of API endpoints for different services
    """

    API_VERSION = "/v2"

    # Pet
    PETS = "/pet"
    PET_ID = "/pet/{pet_id}"
    PET_FIND_BY_STATUS = "/pet/findByStatus"
