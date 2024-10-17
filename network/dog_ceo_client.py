import requests

from contants.base_urls import BaseUrls


class DogCeoClient:
    _base_url: str

    def __init__(self, base_url: str = BaseUrls.DOG_CEO):
        self._base_url = base_url

    def get_sub_breeds(self, breed):
        res = requests.get(f'{self._base_url}/breed/{breed}/list')
        return res.json().get('message', [])

    def get_urls(self, breed, sub_breeds):
        url_images = []
        if sub_breeds:
            for sub_breed in sub_breeds:
                res = requests.get(f"{self._base_url}/breed/{breed}/{sub_breed}/images/random")
                sub_breed_urls = res.json().get('message')
                url_images.append(sub_breed_urls)
        else:
            url_images.append(requests.get(f"{BaseUrls.DOG_CEO}/breed/{breed}/images/random").json().get('message'))

        return url_images
