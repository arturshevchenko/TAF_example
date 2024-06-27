import random

import allure


class EnumUtils:

    @staticmethod
    @allure.step('Get random value from enum')
    def get_random_value(enum_class):
        return random.choice(list(enum_class)).value
