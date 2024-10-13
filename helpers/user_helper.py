import allure
import random
import requests
from helpers.url import *
from helpers.endpoint import *


class ManipulationUserData:
    dict_registration = {}

    @classmethod
    def setup_class(cls):
        alphabet = [chr(i) for i in range(97, 123)]
        cls.dict_registration = {
            'email': (''.join(random.sample(alphabet, 4)) + f'_test_{random.randint(100, 999)}@mail.com'),
            'password': random.randint(100000, 999999),
            'name': (''.join(random.sample(alphabet, 4)) + f'_test_{random.randint(100, 999)}')
        }

    @allure.title('Отправляем POST запрос на создание пользователя с неиспользованными ранее данными')
    def create_user(self):
        payload = {
            'email': self.dict_registration.get('email'),
            'password': self.dict_registration.get('password'),
            'name': self.dict_registration.get('name')
        }
        requests.post(f'{GetUrl.URL}{Endpoint.CREATE_USER}', data=payload)
        return self.dict_registration



    @classmethod
    def teardown_class(cls):
        cls.payload = {
            'email': cls.dict_registration.get('email'),
            'password': cls.dict_registration.get('password'),
        }
        response = requests.post(f'{GetUrl.URL}{Endpoint.LOGIN_USER}', data=cls.payload)
        response_body = response.json()
        requests.delete(f'{GetUrl.URL}{Endpoint.DELETE_USER}',
                        headers={'Authorization': f'{response_body.get("accessToken")}'})
