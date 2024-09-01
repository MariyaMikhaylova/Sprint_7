import allure

from helper import TestDataHelper
from scooter_api import ScooterApi


class TestLogiEndpoints:

    @allure.title('Проверка успешной авторизации курьера')
    def test_successful_login(self, register_new_courier_and_return_login_password):
        courier = register_new_courier_and_return_login_password
        login_body = TestDataHelper.create_login_body(courier[0], courier[1])
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 200

    @allure.title('При передаче пустого поля Логин курьер не будет авторизован')
    def test_login_empty_login(self, register_new_courier_and_return_login_password):
        courier = register_new_courier_and_return_login_password
        login_body = TestDataHelper.create_login_body("", courier[1])
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 400

    @allure.title('При передаче пустого поля Пароль курьер не будет авторизован')
    def test_login_empty_password(self, register_new_courier_and_return_login_password):
        courier = register_new_courier_and_return_login_password
        login_body = TestDataHelper.create_login_body(courier[0], "")
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 400

    @allure.title('Система вернёт ошибку, если неправильно указать Логин при авторизации')
    def test_login_false_login(self, register_new_courier_and_return_login_password):
        courier = register_new_courier_and_return_login_password
        login_body = TestDataHelper.create_login_body("Masha", courier[1])
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 404

    @allure.title('Система вернёт ошибку, если неправильно указать Пароль при авторизации')
    def test_login_false_password(self, register_new_courier_and_return_login_password):
        courier = register_new_courier_and_return_login_password
        login_body = TestDataHelper.create_login_body(courier[0], "112233")
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 404

    @allure.title('Система вернёт ошибку, если не передать Пароль при авторизации')
    def test_login_without_login(self):
        login_body = {"login": "Masha"}
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 400 and login_request.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Система вернёт ошибку, если не передать Логин при авторизации')
    def test_login_without_password(self):
        login_body = {"password": "112233"}
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 400 and login_request.json()["message"] == "Недостаточно данных для входа"

    @allure.title('При авторизации под несуществующим пользователем, запрос возвращает ошибку')
    def test_unknown_courier(self):
        login_body = {"login": "Nobody", "password": "998877", "firstName": "Nobody"}
        login_request = ScooterApi.login(login_body)
        assert login_request.status_code == 404 and login_request.json()["message"] == "Учетная запись не найдена"

    @allure.title('Успешный запрос авторизации возвращает id')
    def test_successful_login_return_id(self, register_new_courier_and_return_login_password):
        courier = register_new_courier_and_return_login_password
        login_body = TestDataHelper.create_login_body(courier[0], courier[1])
        login_request = ScooterApi.login(login_body)
        assert login_request.json()["id"] > 0
