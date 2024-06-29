from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
import os
import requests
from concurrent.futures import ThreadPoolExecutor
from downloader.utils import create_save_directory, get_file_extension, get_sub_directory


@dataclass
class URL:
    url: str


class FileDownloaderBase(ABC):
    @abstractmethod
    def download_file(self, url: str) -> None:
        pass

    @abstractmethod
    def download_files(self, urls: List[URL]) -> None:
        pass


class FileDownloader(FileDownloaderBase):
    def __init__(self, save_dir: str, max_workers: int = 5):
        self.save_dir = save_dir
        self.max_workers = max_workers

    def download_file(self, url: str) -> None:
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
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")

    def download_files(self, urls: List[URL]) -> None:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for file_url in urls:
                executor.submit(self.download_file, file_url.url)
        print("All files downloaded successfully.")
