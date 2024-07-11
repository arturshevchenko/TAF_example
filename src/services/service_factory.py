from src.services.services.pets_service import PetsService


class ServiceFactory:
    @staticmethod
    def pets(session=None):
        return PetsService(session=session)


app_api = ServiceFactory()
