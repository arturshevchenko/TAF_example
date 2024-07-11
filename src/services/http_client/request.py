import requests

from src.configs.config_loader import AppConfigs
from src.configs.endpoint import Endpoint


class Request:
    def __init__(self, session=None):
        self._base_url = AppConfigs.BASE_URL + Endpoint.API_VERSION.value
        self._method = None
        self._path = None
        self._body = None
        self._data = {}
        self._headers = {}
        self._cookies = {}
        self._query_params = {}
        # self._files = []
        self._files = {}
        self._session = session
        # if self._auth_cookie:
        if self._session:
            # self._request = self._session
            self._request = requests
            self.set_headers(**{"Authorization": f"Bearer {self._session}"})
        else:
            self._request = requests

    def clear_session(self):
        self._session = None
        return self

    def set_base_url(self, base_url):
        self._base_url = base_url
        return self

    def set_path(self, path):
        self._path = path
        return self

    def set_method(self, method):
        self._method = method.value
        return self

    def set_body(self, body):
        self._body = body
        return self

    def set_form_data(self, **data):
        self._data.update(data)
        return self

    def set_headers(self, **headers):
        self._headers.update(headers)
        return self

    def set_cookies(self, **cookies):
        self._cookies.update(cookies)
        return self

    def set_query_params(self, **query_params):
        self._query_params.update(query_params)
        return self

    def set_files(self, **file):
        self._files.update(file)
        return self

    def request_payload(self):
        return {
            "url": self._base_url + self._path,
            "json": self._body,
            "data": self._data,
            "headers": self._headers,
            "params": self._query_params,
            "cookies": self._cookies,
            "files": self._files,
        }

    def send(self):
        return self._request.request(
            self._method, **self.request_payload(), allow_redirects=True
        )

    def post(self):
        return self._request.post(**self.request_payload(), allow_redirects=True)

    def get(self):
        return self._request.get(**self.request_payload(), allow_redirects=True)
