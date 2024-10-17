import requests

from contants.base_urls import BaseUrls


class DogCeoClient:
    _base_url: str = BaseUrls.DOG_CEO

    def get_sub_breeds(self, breed: str) -> list[str]:
        response = requests.get(f'{self._base_url}/breed/{breed}/list')
        return response.json().get('message', [])

    def get_urls(self, breed: str, sub_breeds: list[str]) -> list[str]:
        url_images = []
        if sub_breeds:
            for sub_breed in sub_breeds:
                response = requests.get(f"{self._base_url}/breed/{breed}/{sub_breed}/images/random")
                sub_breed_urls = response.json().get('message')
                url_images.append(sub_breed_urls)
        else:
            url_images.append(requests.get(f"{self._base_url}/breed/{breed}/images/random").json().get('message'))

        return url_images
