from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass
import instaloader


@dataclass
class InstagramURL:
    url: str


class InstagramDownloaderBase(ABC):
    @abstractmethod
    def download_post(self, url: str) -> None:
        pass

    @abstractmethod
    def download_posts(self, urls: List[InstagramURL]) -> None:
        pass


class InstagramDownloader(InstagramDownloaderBase):
    def __init__(self, save_dir: str, max_workers: int = 5):
        self.save_dir = save_dir
        self.max_workers = max_workers
        self.loader = instaloader.Instaloader(dirname_pattern=self.save_dir)

    def download_post(self, url: str) -> None:
        try:
            post = instaloader.Post.from_shortcode(
                self.loader.context, url.split('/')[-2]
            )
            self.loader.download_post(post, target=self.save_dir)
            print(f"Downloaded Instagram post {post.shortcode} successfully.")
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")

    def download_posts(self, urls: List[InstagramURL]) -> None:
        for instagram_url in urls:
            self.download_post(instagram_url.url)
        print("All Instagram posts downloaded successfully.")
