from contants.test_constants import TEST_FOLDER
from network.dog_ceo_client import DogCeoClient
from network.ya_uploader import YaUploader


def upload_photos(breed: str, base_folder_name: str = TEST_FOLDER):
    dog_ceo_client = DogCeoClient()
    ya_uploader = YaUploader()

    sub_breeds = dog_ceo_client.get_sub_breeds(breed)
    urls = dog_ceo_client.get_urls(breed, sub_breeds)

    ya_uploader.create_folder(base_folder_name)

    for url in urls:
        part_name = url.split('/')
        name = '_'.join([part_name[-2], part_name[-1]])
        ya_uploader.upload_photos_to_yd(base_folder_name, url, name)
