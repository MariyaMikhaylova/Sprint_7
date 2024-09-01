import requests
import urls


class ScooterApi:

    @staticmethod
    def registration(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    def registration_short(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    def login(body):
        return requests.post(urls.BASE_URL + urls.LOGIN_COURIER_ENDPOINT, json=body)

    @staticmethod
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    def get_order_list():
        return requests.get(urls.BASE_URL + urls.GET_ORDER_LIST_ENDPOINT)
