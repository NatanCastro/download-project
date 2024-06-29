from typing import List
from downloader.downloaders.files import URL
from downloader.downloaders.youtube import YouTubeURL
from downloader.downloaders.instagram import InstagramURL
from downloader.downloader_factory import DownloaderFactory


class DownloadManager:
    def __init__(self, factory: DownloaderFactory):
        self.file_downloader = factory.create_file_downloader(save_dir='files')
        self.youtube_downloader = factory.create_youtube_downloader(
            save_dir='youtube_videos')
        self.instagram_downloader = factory.create_instagram_downloader(
            save_dir='instagram_posts')
        self.file_urls: List[URL] = []
        self.youtube_urls: List[YouTubeURL] = []
        self.instagram_urls: List[InstagramURL] = []

    def add_file_url(self, url: str) -> None:
        self.file_urls.append(URL(url))

    def add_youtube_url(self, url: str) -> None:
        self.youtube_urls.append(YouTubeURL(url))

    def add_instagram_url(self, url: str) -> None:
        self.instagram_urls.append(InstagramURL(url))

    def download_all(self) -> None:
        if self.file_urls:
            self.file_downloader.download_files(self.file_urls)
        if self.youtube_urls:
            self.youtube_downloader.download_videos(self.youtube_urls)
        if self.instagram_urls:
            self.instagram_downloader.download_posts(self.instagram_urls)
