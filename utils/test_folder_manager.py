import traceback
import uuid

from network.ya_uploader import YaUploader


class TestFolderManager:
    created_folders = []

    @staticmethod
    def get_unique_test_folder() -> str:
        new_folder = f"test_folder_{uuid.uuid4()}"
        TestFolderManager.created_folders.append(new_folder)

        return new_folder

    @staticmethod
    def delete_all_folders():
        for folder in TestFolderManager.created_folders:
            try:
                YaUploader().delete_folder(folder, True)
            except Exception:
                print(f"Failed to delete folder: {folder}")
                print(traceback.format_exc())
