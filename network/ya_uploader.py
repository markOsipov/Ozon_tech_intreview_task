import requests

from contants.api_constants import ApiConstants
from contants.base_urls import BaseUrls


class YaUploader:
    _token: str
    _default_headers: dict

    def __init__(self, token: str = ApiConstants.YANDEX_OAUTH_TOKEN):
        self._token = token
        self._default_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def create_folder(self, path):
        url_create = f'{BaseUrls.YANDEX_DRIVE}/resources'
        headers = self._default_headers

        response = requests.put(f'{url_create}?path={path}', headers=headers)

        return response.json()

    def upload_photos_to_yd(self, path, url_file, name):
        url = f'{BaseUrls.YANDEX_DRIVE}/resources/upload'
        headers = self._default_headers
        params = {"path": f'/{path}/{name}', 'url': url_file, "overwrite": "true"}

        response = requests.post(url, headers=headers, params=params)

        return response.json()