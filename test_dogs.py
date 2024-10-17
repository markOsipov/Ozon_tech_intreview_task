import random

import pytest
from network.dog_ceo_client import DogCeoClient
from network.ya_uploader import YaUploader





def u(breed):
    dog_ceo_client = DogCeoClient()
    sub_breeds = dog_ceo_client.get_sub_breeds(breed)
    urls = dog_ceo_client.get_urls(breed, sub_breeds)
    yandex_client = YaUploader()
    yandex_client.create_folder('test_folder')

    for url in urls:
        part_name = url.split('/')
        name = '_'.join([part_name[-2], part_name[-1]])
        yandex_client.upload_photos_to_yd("test_folder", url, name)


@pytest.mark.parametrize('breed', ['doberman', random.choice(['bulldog', 'collie'])])
def test_upload_dog_no_sub_breeds(breed):
    u(breed)

    uploader = YaUploader()
    dog_ceo_client = DogCeoClient()

    response = uploader.create_folder("test_folder")
    assert response['type'] == "dir"
    assert response['name'] == "test_folder"

    items = response['_embedded']['items']
    breeds = dog_ceo_client.get_sub_breeds(breed)

    if not breeds:
        assert len(items) == 1
    else:
        assert len(items) == len(breeds)

    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)


@pytest.mark.parametrize('breed', ['bulldog', 'collie'])
def test_upload_dog_with_sub_breeds(breed):
    u(breed)

    uploader = YaUploader()
    dog_ceo_client = DogCeoClient()

    response = uploader.create_folder("test_folder")
    assert response['type'] == "dir"
    assert response['name'] == "test_folder"

    items = response['_embedded']['items']
    breeds = dog_ceo_client.get_sub_breeds(breed)

    assert len(breeds) > 0
    assert len(items) == len(breeds)

    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)
