import requests
from requests import Response

from contants.api_constants import ApiConstants
from contants.base_urls import BaseUrls


class YaUploader:
    _token: str
    _default_headers: dict
    _base_url = BaseUrls.YANDEX_DRIVE

    def __init__(self,  token: str = ApiConstants.YANDEX_OAUTH_TOKEN):
        self._token = token
        self._default_headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token}'
        }

    def create_folder(self, path: str) -> dict:
        url = f'{self._base_url}/resources'
        headers = self._default_headers
        params = {'path': path}
        response = requests.put(url, headers=headers, params=params)

        return response.json()

    def get_folder(self, path: str) -> dict:
        url = f'{self._base_url}/resources'
        headers = self._default_headers
        params = {'path': path}
        response = requests.get(url, headers=headers, params=params)

        return response.json()

    def delete_folder(self, path: str, permanently: bool = True) -> Response:
        url = f'{self._base_url}/resources'
        headers = self._default_headers
        params = {'path': path, 'permanently': permanently}
        response = requests.delete(url, headers=headers, params=params)

        return response

    def upload_photos_to_yd(self, path: str, url_file: str, name: str) -> dict:
        url = f'{self._base_url}/resources/upload'
        headers = self._default_headers
        params = {"path": f'/{path}/{name}', 'url': url_file, "overwrite": "true"}

        response = requests.post(url, headers=headers, params=params)

        return response.json()
