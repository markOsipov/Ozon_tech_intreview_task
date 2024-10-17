from time import sleep

import pytest
from network.dog_ceo_client import DogCeoClient
from network.ya_uploader import YaUploader
from utils.test_folder_manager import TestFolderManager
from utils.upload_photos import upload_photos


@pytest.mark.parametrize("breed", ["doberman"])
def test_upload_dog_no_sub_breeds(breed: str):
    ya_uploader = YaUploader()
    dog_ceo_client = DogCeoClient()
    test_folder = TestFolderManager.get_unique_test_folder()

    upload_photos(breed, test_folder)

    sleep(1)
    yd_folder = ya_uploader.get_folder(test_folder)

    assert yd_folder['type'] == "dir"
    assert yd_folder['name'] == test_folder

    items = yd_folder['_embedded']['items']
    breeds = dog_ceo_client.get_sub_breeds(breed)

    assert len(breeds) == 0
    assert len(items) == 1

    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)


@pytest.mark.parametrize('breed', ['bulldog', 'collie'])
def test_upload_dog_with_sub_breeds(breed: str):
    ya_uploader = YaUploader()
    dog_ceo_client = DogCeoClient()
    test_folder = TestFolderManager.get_unique_test_folder()

    upload_photos(breed, test_folder)

    sleep(1)
    yd_folder = ya_uploader.get_folder(test_folder)

    assert yd_folder['type'] == "dir"
    assert yd_folder['name'] == test_folder

    items = yd_folder['_embedded']['items']
    breeds = dog_ceo_client.get_sub_breeds(breed)

    assert len(breeds) > 0
    assert len(items) == len(breeds)

    for item in items:
        assert item['type'] == 'file'
        assert item['name'].startswith(breed)
