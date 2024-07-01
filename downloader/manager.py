from typing import List
from downloader.downloader_factory import DownloaderFactory
from downloader.status_manager import StatusManager


class DownloadManager:
    def __init__(self, factory: DownloaderFactory):
        self.status_manager = StatusManager()
        self.file_downloader = factory.create_file_downloader(
            save_dir='files', manager=self.status_manager)
        self.youtube_downloader = factory.create_youtube_downloader(
            save_dir='youtube_videos', manager=self.status_manager)
        self.instagram_downloader = factory.create_instagram_downloader(
            save_dir='instagram_posts', manager=self.status_manager)
        self.file_urls: List[str] = []
        self.youtube_urls: List[str] = []
        self.instagram_urls: List[str] = []

    def add_file_url(self, url: str) -> None:
        self.file_urls.append(url)
        self.status_manager.update_status(url, 'Pending')

    def add_youtube_url(self, url: str) -> None:
        self.youtube_urls.append(url)
        self.status_manager.update_status(url, 'Pending')

    def add_instagram_url(self, url: str) -> None:
        self.instagram_urls.append(url)
        self.status_manager.update_status(url, 'Pending')

    def remove_download(self, url: str) -> None:
        if url in self.file_urls:
            self.file_urls.remove(url)
        if url in self.youtube_urls:
            self.youtube_urls.remove(url)
        if url in self.instagram_urls:
            self.instagram_urls.remove(url)
        self.status_manager.remove_status(url)

    def update_status(self, url: str, name: str, status: str) -> None:
        self.status_manager.update_status(url, f"{name[:10]}: {status}")

    def download_all(self) -> None:
        if self.file_urls:
            self.file_downloader.download_files(self.file_urls)
        if self.youtube_urls:
            self.youtube_downloader.download_videos(self.youtube_urls)
        if self.instagram_urls:
            self.instagram_downloader.download_posts(self.instagram_urls)
