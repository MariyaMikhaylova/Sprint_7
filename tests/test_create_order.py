import allure
import pytest
from scooter_api import ScooterApi


class TestOrder:

    @allure.title('Чекпоинт "Цвет" не влияет на возможность оформления заказа')
    @pytest.mark.parametrize('firstName,lastName,address,metroStation,phone,rentTime,deliveryDate,comment,color',
                             [
                                 ["Masha", "Student", "My Street, 1", 22, "+7 111 222 33 44", 2, "2024-09-09", "Go", ["BLACK"]],
                                 ["Masha", "Student", "My Street, 1", 22, "+7 111 222 33 44", 2, "2024-09-09", "Go", ["GREY"]],
                                 ["Masha", "Student", "My Street, 1", 22, "+7 111 222 33 44", 2, "2024-09-09", "Go", ["BLACK","GREY"]],
                                 ["Masha", "Student", "My Street, 1", 22, "+7 111 222 33 44", 2, "2024-09-09", "Go", []]
                             ]
                             )
    def test_create_order_scooter_color(self, firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):
        body = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        login_request = ScooterApi.create_order(body)
        assert login_request.status_code == 201

    @allure.title('После создания заказа в теле ответа возвращается трек-номер')
    def test_create_order_return_track(self, create_order_empty_color):
        login_request = ScooterApi.create_order(create_order_empty_color)
        assert login_request.json()['track'] > 0
