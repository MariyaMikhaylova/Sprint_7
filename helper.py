from faker import Faker
from data import TestUserData


class TestDataHelper:
    @staticmethod
    def modify_registration_body_request(key, value):
        body = TestUserData.REGISTRATION_USER_BODY.copy()
        body[key] = value
        return body

    @classmethod
    def create_registration_body(cls):
        fake = Faker()
        return TestDataHelper.modify_registration_body_request("login", fake.name())

    @classmethod
    def create_login_body(cls, login, password):
        body = TestUserData.LOGIN_USER_BODY.copy()
        body["login"] = login
        body["password"] = password
        return body

    @staticmethod
    def modify_registration_body_short_request(key, value):
        body = TestUserData.REGISTRATION_USER_BODY_SHORT.copy()
        body[key] = value
        return body

    @classmethod
    def create_registration_body_short(cls):
        fake = Faker()
        return TestDataHelper.modify_registration_body_short_request("login", fake.name())

    @staticmethod
    def modify_registration_body_empty_password_request(key, value):
        body = TestUserData.REGISTRATION_USER_BODY_EMPTY_PASSWORD.copy()
        body[key] = value
        return body

    @classmethod
    def create_registration_body_empty_password(cls):
        fake = Faker()
        return TestDataHelper.modify_registration_body_empty_password_request("login", fake.name())

    @staticmethod
    def modify_registration_body_without_password_request(key, value):
        body = TestUserData.REGISTRATION_USER_BODY_WITHOUT_PASSWORD.copy()
        body[key] = value
        return body

    @classmethod
    def create_registration_body_without_password(cls):
        fake = Faker()
        return TestDataHelper.modify_registration_body_empty_password_request("login", fake.name())

    @staticmethod
    def modify_registration_body_without_login_request(key, value):
        body = TestUserData.REGISTRATION_USER_BODY_WITHOUT_LOGIN
        body[key] = value
        return body

    @classmethod
    def create_registration_body_without_login(cls):
        fake = Faker()
        return TestDataHelper.modify_registration_body_empty_password_request("login", fake.name())
