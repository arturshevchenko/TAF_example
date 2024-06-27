import json
import logging
from datetime import datetime
from json import JSONDecodeError

import allure
import requests
from curlify2 import Curlify

from src.configs.colors import Colors
from src.configs.config_loader import AppConfigs


class AssertableResponse(object):

    def __init__(self, response: requests.Response):
        if AppConfigs.LOGS:
            logging.info(f"{Colors.Red}get at {datetime.now()}{Colors.Reset}")
            # filter bytes in logs

            request_body = ""
            if "name=\"file\"" not in str(response.request.body):
                if response.request.body:
                    try:
                        request_body = json.dumps(json.loads(response.request.body), indent=6)
                        curl = Curlify(response.request).to_curl()
                    except JSONDecodeError:
                        request_body = response.request.body
                        curl = Curlify(response.request).to_curl()
                else:
                    curl = Curlify(response.request).to_curl()

                logging.info(
                        f"\n{Colors.Yellow}Request{Colors.Reset}"
                        f"\n\t{Colors.Yellow}CURL: {Colors.Reset}"
                        f"\n{Colors.Green}\n{curl}\n{Colors.Reset}\n"
                        f"\n\t{Colors.Yellow}method = {response.request.method}{Colors.Reset}"
                        f"\n\t{Colors.Yellow}url = {response.request.url}{Colors.Reset}"
                        f"\n\t{Colors.Yellow}body = \n{request_body}{Colors.Reset}"
                )
            else:
                logging.info(
                        f"\n{Colors.Yellow}Request{Colors.Reset}"
                        f"\n\t{Colors.Yellow}method = {response.request.method}{Colors.Reset}"
                        f"\n\t{Colors.Yellow}url = {response.request.url}{Colors.Reset}"
                        f"\n\t{Colors.Yellow}file = binary data{Colors.Reset}"
                )

            try:
                response_body = json.dumps(json.loads(response.text), indent=6)
            except JSONDecodeError:
                response_body = response.text

            logging.info(
                    f"\n{Colors.Yellow}Response{Colors.Reset}"
                    f"\n\t{Colors.Yellow}status_code = {response.status_code} {response.reason}{Colors.Reset}"
                    f"\n\t{Colors.Yellow}body = \n{response_body}\n\n{Colors.Reset}"
            )

        allure.attach(
                f"\nRequest \n "
                f"url = {response.request.url} \n "
                f"body = {response.request.body}",
                "request.txt",
                allure.attachment_type.TEXT
        )
        allure.attach(
                f"\nResponse \n "
                f"status = {response.status_code} \n "
                f"body = {response.text}",
                "response.txt",
                allure.attachment_type.TEXT
        )
        self._response = response

    @allure.step('status code should be "{code}"')
    def status_code(self, code):
        if AppConfigs.LOGS:
            logging.info(f"{Colors.Magenta}ASSERT: Status code should be {code}{Colors.Reset}")
        return self._response.status_code == code

    @allure.step('Check: response should have {condition}')
    def should_have(self, *condition):
        for condition_arg in condition:
            if AppConfigs.LOGS:
                logging.info(f"{Colors.Magenta}Check: {str(condition_arg)}{Colors.Reset}")
            condition_arg.match(self._response)
        return self

    @allure.step('Check: response does not have {condition}')
    def should_not_have(self, condition):
        if AppConfigs.LOGS:
            logging.info(f"{Colors.Magenta}Check not contains: {str(condition)}{Colors.Reset}")
        condition.not_presented(self._response)
        return self

    @allure.step('Check: response contains {condition}')
    def should_contain(self, *condition):
        for condition_arg in condition:
            if AppConfigs.LOGS:
                logging.info(f"{Colors.Magenta}Check: {str(condition_arg)}{Colors.Reset}")
            condition_arg.contains(self._response)
        return self

    @allure.step('get field "{name}"')
    def get_field(self, name):
        return self._response.json()[name]

    @allure.step('get json from response')
    def get_json(self):
        return self._response.json()

    @allure.step('get status code from response')
    def get_status(self):
        return self._response.status_code

    @allure.step('get json from response as text')
    def get_body(self):
        return self._response.text

    @allure.step('get content from response as text')
    def get_content(self):
        return self._response.content

    @allure.step('get cookies from response')
    def get_cookies(self):
        return self._response.cookies

    @allure.step('get headers from response')
    def get_headers(self):
        return self._response.headers
