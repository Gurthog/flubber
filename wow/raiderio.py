"""
RaiderIO API Utilities

https://raider.io/api
"""
import requests


BASE_URL = 'https://raider.io/api/v1'


def get_character(name: str, realm: str) -> dict:
    endpoint = '/characters/profile'
    url = f'{BASE_URL}{endpoint}'
    params = {
        'name': name,
        'realm': realm,
        'region': 'us',
    }
    response = requests.get(url, params=params)

    if not response.ok:
        response.raise_for_status()

    return response.json()

