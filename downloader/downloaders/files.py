from typing import List
import os
import requests
from concurrent.futures import ThreadPoolExecutor
from downloader.utils import create_save_directory, get_file_extension, get_sub_directory
from downloader.status_manager import StatusManager


class FileDownloader:
    def __init__(self, save_dir: str, manager: StatusManager, max_workers: int = 5):
        self.save_dir = save_dir
        self.manager = manager
        self.max_workers = max_workers

    def download_file(self, url: str) -> str:
        try:
            response = requests.get(url)
            file_extension = get_file_extension(url)
            sub_dir = get_sub_directory(file_extension)
            dir_path = create_save_directory(self.save_dir, sub_dir)
            file_name = os.path.basename(url)
            file_path = os.path.join(dir_path, file_name)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {file_name} successfully to {sub_dir}")
            return file_name
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")
            return None

    def download_files(self, urls: List[str]) -> None:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for file_url in urls:
                executor.submit(self._download_and_update_status, file_url)
        print("All files downloaded successfully.")

    def _download_and_update_status(self, url: str) -> None:
        file_name = self.download_file(url)
        if file_name:
            self.manager.update_status(url, file_name, 'Completed')
        else:
            self.manager.update_status(url, file_name, 'Failed')
