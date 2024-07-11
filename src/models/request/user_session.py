import requests


class UserSession:
    @staticmethod
    def create_session():
        return requests.Session()
