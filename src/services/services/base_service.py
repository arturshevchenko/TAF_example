from src.configs.config_loader import AppConfigs
from src.configs.endpoint import Endpoint
from src.services.http_client.request import Request


class BaseService:

    def __init__(self, session=None):
        self._request: Request = Request(session)
        self._request \
            .set_base_url(AppConfigs.BASE_URL + Endpoint.API_VERSION.value)

    def set_base_url(self, new_url):
        self._request.set_base_url(new_url)
        return self

    def set_headers(self, **headers):
        self._request.set_headers(**headers)
        return self

    def remove_auth(self):
        self._request.clear_session()
        return self

    def set_internal_auth(self, auth_header):
        self._request.set_headers(**{'x-api-key': auth_header})
        return self

    def remove_internal_auth(self):
        self._request.set_headers(**{'x-api-key': None})
        return self
