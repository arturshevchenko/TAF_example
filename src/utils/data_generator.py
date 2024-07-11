import random
import secrets
import string
from uuid import uuid4

import allure


class DataGenerator:
    @staticmethod
    @allure.step("Random boolean")
    def random_boolean():
        return bool(random.randint(0, 1))

    @staticmethod
    @allure.step("Random float 2 decimals")
    def random_float(minimum, maximum):
        return round(random.uniform(minimum, maximum), 2)

    @staticmethod
    @allure.step("Random int")
    def random_int(minimum, maximum):
        return random.randint(minimum, maximum)

    @staticmethod
    @allure.step("Random hex {length} symbols")
    def hex_of(length):
        return secrets.token_hex(length).upper()

    @staticmethod
    @allure.step("Random uuid v4")
    def random_uuid4():
        return str(uuid4())

    @staticmethod
    @allure.step("Generate random password")
    def password():
        return DataGenerator.string_of(random.randint(8, 60))

    @staticmethod
    @allure.step("Generate random email")
    def email():
        return "ttmi.test.driver+{0}@gmail.com".format(
            DataGenerator.string_numbers_of(15)
        )

    @staticmethod
    @allure.step("Generate random phone")
    def phone_number():
        return "+38063" + DataGenerator.string_numbers_of(7)

    @staticmethod
    @allure.step("Generate random phone USA")
    def usa_phone_number():
        return "+14155" + DataGenerator.string_numbers_of(6)

    @staticmethod
    @allure.step("Random string upper and lower letters of {length} symbols")
    def string_of(length):
        key = ""
        for _ in range(length):
            key += random.choice(string.ascii_letters)
        return str(key)

    @staticmethod
    @allure.step("Random numeric string of {length} symbols")
    def string_numbers_of(length):
        key = ""
        for _ in range(length):
            key += random.choice(string.digits)
        return str(key)

    @staticmethod
    @allure.step("Random spec-chars string of {length} symbols")
    def string_only_spec_chars_of(length):
        # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        key = ""
        for _ in range(length):
            key += random.choice(string.punctuation)
        return str(key)

    @staticmethod
    @allure.step("Random alpha-numeric string of {length} symbols")
    def string_alphanumeric_of(length):
        key = ""
        for _ in range(length):
            key += random.choice(string.ascii_letters + string.digits)
        return str(key)

    @staticmethod
    @allure.step("Random string with spec-chars of {length} symbols")
    def string_with_spec_chars_of(length):
        # '0123456789
        # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        key = ""
        for _ in range(length):
            key += random.choice(
                string.ascii_letters + string.digits + string.punctuation
            )
        return str(key)

    @staticmethod
    @allure.step("Random string with spec-chars and whitespace of {length} symbols")
    def string_with_allchars_of(length):
        # '0123456789
        # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
        # \t\n\r\x0b\x0c'
        key = ""
        for _ in range(length):
            key += random.choice(string.printable + " ")
        return str(key).strip()

    @staticmethod
    @allure.step("String of chars numbs dash dot hyhpen")
    def string_alphanumeric_dash_dot_huphen(length):
        key = ""
        for _ in range(length):
            key += random.choice(string.ascii_letters + string.digits + "-_.")
        return str(key)

    @staticmethod
    @allure.step("String of chars numbs +=,.@-")
    def string_alphanumeric_sso_provider(length):
        key = ""
        for _ in range(length):
            key += random.choice(string.ascii_letters + string.digits + "+=,.@-")
        return str(key)

    @staticmethod
    def string_user_full_name(length):
        key = ""
        for _ in range(length):
            key += random.choice(string.ascii_letters + string.digits + "+=.@-_")
        return str(key)

    @staticmethod
    @allure.step("String of invalid vehicle plate chars")
    def string_spec_chars_not_dash_dot_hyphen():
        return "!\"#$%&'()*+,/:;<=>?@[\\]^`{|}~"

    class Thai:
        thai_characters = [
            "ก",
            "ข",
            "ค",
            "ฆ",
            "ง",
            "จ",
            "ฉ",
            "ช",
            "ซ",
            "ฌ",
            "ญ",
            "ฎ",
            "ฏ",
            "ฐ",
            "ฑ",
            "ฒ",
            "ณ",
            "ด",
            "ต",
            "ถ",
            "ท",
            "ธ",
            "น",
            "บ",
            "ป",
            "ผ",
            "ฝ",
            "พ",
            "ฟ",
            "ภ",
            "ม",
            "ย",
            "ร",
            "ล",
            "ว",
            "ศ",
            "ษ",
            "ส",
            "ห",
            "ฬ",
            "อ",
            "ฮ",
        ]

        @classmethod
        @allure.step("Random string upper and lower letters of {length} symbols")
        def string_of(cls, length):
            key = ""
            for _ in range(length):
                key += random.choice(cls.thai_characters)
            return str(key)

        @classmethod
        @allure.step("Random alpha-numeric string of {length} symbols")
        def string_alphanumeric_of(cls, length):
            key = ""
            for _ in range(length):
                key += random.choice("".join(cls.thai_characters) + string.digits)
            return str(key)

        @classmethod
        @allure.step("Random string with spec-chars of {length} symbols")
        def string_with_spec_chars_of(cls, length):
            # '0123456789
            # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
            # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
            key = ""
            for _ in range(length):
                key += random.choice(
                    "".join(cls.thai_characters) + string.digits + string.punctuation
                )
            return str(key)

        @classmethod
        @allure.step("Random string with spec-chars and whitespace of {length} symbols")
        def string_with_allchars_of(cls, length):
            # '0123456789
            # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
            # !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
            # \t\n\r\x0b\x0c'
            key = ""
            for _ in range(length):
                key += random.choice(
                    "".join(cls.thai_characters)
                    + " "
                    + string.digits
                    + string.punctuation
                )
            return str(key).strip()

        @classmethod
        @allure.step("String of chars numbs dash dot hyhpen")
        def string_alphanumeric_dash_dot_huphen(cls, length):
            key = ""
            for _ in range(length):
                key += random.choice(
                    "".join(cls.thai_characters) + string.digits + "-_."
                )
            return str(key)
