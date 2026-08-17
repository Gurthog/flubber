"""
RaiderIO API Utilities

https://raider.io/api
"""
import os
import requests


BASE_URL = 'https://raider.io/api/v1'
KEY = os.getenv('RAIDER_IO_KEY')


def get_character(name: str, realm: str, fields: list[str] = []):
    endpoint = '/characters/profile'
    url = f'{BASE_URL}{endpoint}'

    params = {
        'name': name,
        'realm': realm,
        'region': 'us',
    }
    if fields:
        params['fields'] = ','.join(fields)
    if KEY:
        params['access_key'] = KEY

    response = requests.get(url, params=params)

    if not response.ok:
        response.raise_for_status()

    return response.json()




if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    data = get_character(
        'bungle',
        'khaz-modan',
        fields = [
            'guild',
            'mythic_plus_dungeon_run_counts',
            'mythic_plus_recent_runs',
        ],
    )
    print(data)

