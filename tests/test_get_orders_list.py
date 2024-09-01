import allure
from scooter_api import ScooterApi


@allure.title('На запрос списка заказов в тело ответа возвращается список заказов')
def test_get_orders_list(create_order_empty_color):
    ScooterApi.create_order(create_order_empty_color)
    login_request = ScooterApi.get_order_list()
    assert len(login_request.json()["orders"]) > 0
