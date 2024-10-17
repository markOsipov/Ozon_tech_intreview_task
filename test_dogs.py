from time import sleep

import pytest

from contants.breeds import Breeds
from network.dog_ceo_client import DogCeoClient
from network.ya_uploader import YaUploader
from utils.test_folder_manager import TestFolderManager
from utils.upload_photos import upload_photos
from utils.wait_for_condiion import wait_for_condition


@pytest.mark.parametrize("breed", [Breeds.DOBERMAN])
def test_upload_dog_no_sub_breeds(breed: str):
    ya_uploader = YaUploader()
    dog_ceo_client = DogCeoClient()
    test_folder = TestFolderManager.get_unique_test_folder()

    upload_photos(breed, test_folder)

    breeds = dog_ceo_client.get_sub_breeds(breed)
    assert len(breeds) == 0

    yd_folder = wait_for_condition(
        "Yandex folder contains items",
        action=lambda: ya_uploader.get_folder(test_folder),
        condition=lambda result: len(result['_embedded']['items']) > 0
    )

    assert yd_folder['type'] == "dir"
    assert yd_folder['name'] == test_folder

    items = yd_folder['_embedded']['items']
    assert len(items) == 1

    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)


@pytest.mark.parametrize('breed', [Breeds.BULLDOG, Breeds.COLLIE])
def test_upload_dog_with_sub_breeds(breed: str):
    ya_uploader = YaUploader()
    dog_ceo_client = DogCeoClient()
    test_folder = TestFolderManager.get_unique_test_folder()

    upload_photos(breed, test_folder)

    breeds = dog_ceo_client.get_sub_breeds(breed)
    assert len(breeds) > 0

    yd_folder = wait_for_condition(
        "Yandex folder contains items",
        action=lambda: ya_uploader.get_folder(test_folder),
        condition=lambda result: len(result['_embedded']['items']) == len(breeds)
    )

    assert yd_folder['type'] == "dir"
    assert yd_folder['name'] == test_folder

    items = yd_folder['_embedded']['items']

    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)
