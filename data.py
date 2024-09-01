class TestUserData:

    REGISTRATION_USER_BODY = {
        "login": "",
        "password": "112233",
        "firstName": "Masha"
    }

    LOGIN_USER_BODY = {
        "login": "",
        "password": ""
    }

    REGISTRATION_USER_BODY_SHORT = {
        "login": "",
        "password": "112233"
    }

    REGISTRATION_USER_BODY_EMPTY_PASSWORD = {
        "login": "",
        "password": "",
        "firstName": "Masha"
    }

    REGISTRATION_USER_BODY_WITHOUT_PASSWORD = {
        "login": "",
        "firstName": "Masha"
    }

    REGISTRATION_USER_BODY_WITHOUT_LOGIN = {
        "password": "",
        "firstName": "Masha"
    }

class TestOrderData:

    ORDER_BODY_EMPTY_COLOR = {
        "firstName": "Masha",
        "lastName": "Student",
        "address": "My Street, 1",
        "metroStation": 22,
        "phone": "+7 111 222 33 44",
        "rentTime": 2,
        "deliveryDate": "2024-09-09",
        "comment": "Go",
        "color": []
    }
