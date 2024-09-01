import allure

from data import TestUserData
from helper import TestDataHelper
from scooter_api import ScooterApi


class TestCourierEndpoints:

    @allure.title('Проверка успешной регистрации курьера')
    def test_successful_registration(self):
        registration_request = ScooterApi.registration(TestDataHelper.create_registration_body())
        assert registration_request.json()["ok"]

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_registration_twice_false(self):
        a = TestDataHelper.create_registration_body()
        first_registration_request = ScooterApi.registration(a)
        assert first_registration_request.status_code == 201
        second_registration_request = ScooterApi.registration(a)
        assert second_registration_request.status_code == 409

    @allure.title('При передаче пустого поля Имя курьер будет создан')
    def test_registration_empty_first_name(self):
        registration_request = ScooterApi.registration_short(TestDataHelper.create_registration_body_short())
        assert registration_request.json()["ok"]

    @allure.title('При передаче пустого поля Логин курьер не будет создан')
    def test_registration_empty_login_false(self):
        registration_request = ScooterApi.registration(TestUserData.REGISTRATION_USER_BODY)
        assert registration_request.status_code == 400 and registration_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('При передаче пустого поля Пароль курьер не будет создан')
    def test_registration_empty_password_false(self):
        registration_request = ScooterApi.registration(TestDataHelper.create_registration_body_empty_password())
        assert registration_request.status_code == 400 and registration_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('При успешной регистрации курьера возвращается код 201')
    def test_successful_registration_status_code(self):
        registration_request = ScooterApi.registration(TestDataHelper.create_registration_body())
        assert registration_request.status_code == 201

    @allure.title('При успешной регистрации курьера в теле ответа возвращается ok')
    def test_successful_registration_text(self):
        registration_request = ScooterApi.registration(TestDataHelper.create_registration_body())
        assert registration_request.json()["ok"]

    @allure.title('При передаче пустого поля Логин курьер не будет создан')
    def test_registration_without_login_false(self):
        registration_request = ScooterApi.registration(TestUserData.REGISTRATION_USER_BODY_WITHOUT_LOGIN)
        assert registration_request.status_code == 400 and registration_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Система вернёт ошибку, если не передать Пароль при регистрации')
    def test_registration_without_password_false(self):
        registration_request = ScooterApi.registration(TestDataHelper.create_registration_body_without_password())
        assert registration_request.status_code == 400 and registration_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('При создании пользователя с логином, который уже есть, возвращается ошибка')
    def test_registration_twice_false_text(self):
        a = TestDataHelper.create_registration_body()
        first_registration_request = ScooterApi.registration(a)
        assert first_registration_request.status_code == 201
        second_registration_request = ScooterApi.registration(a)
        assert second_registration_request.json()["message"] == "Этот логин уже используется"
