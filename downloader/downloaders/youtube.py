from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor
from downloader.utils import create_save_directory


@dataclass
class YouTubeURL:
    url: str


class YouTubeDownloaderBase(ABC):
    @abstractmethod
    def download_video(self, url: str) -> None:
        pass

    @abstractmethod
    def download_videos(self, urls: List[YouTubeURL]) -> None:
        pass


class YouTubeDownloader(YouTubeDownloaderBase):
    def __init__(self, save_dir: str, max_workers: int = 5):
        self.save_dir = save_dir
        self.max_workers = max_workers

    def download_video(self, url: str) -> None:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            dir_path = create_save_directory(self.save_dir)
            file_path = stream.download(output_path=dir_path)
            print(f"Downloaded {yt.title} successfully to {file_path}")
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")

    def download_videos(self, urls: List[YouTubeURL]) -> None:
        create_save_directory(self.save_dir)
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for youtube_url in urls:
                executor.submit(self.download_video, youtube_url.url)
        print("All YouTube videos downloaded successfully.")
