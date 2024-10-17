import pytest

from utils.test_folder_manager import TestFolderManager


@pytest.fixture(scope='session', autouse=True)
def clear_test_folder():
    yield
    TestFolderManager.delete_all_folders()
