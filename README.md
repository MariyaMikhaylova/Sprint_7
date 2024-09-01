# В проекте автоматизиронные проверки API сайта Яндекс.Самокат https://qa-scooter.praktikum-services.ru/
# Для запуска тестирования необходимо установить библиотеки pytest, Faker, requests, random, string
# Для формирования отчета необходимо установить библиотеку allure-pytest

# Два теста Faled:
- test_registration_twice_false_text - баг: Текст ошибки в приложении не соответствует тексту ошибки в документации API
- test_login_without_login - баг: сервер возвращает 504 ошибку
