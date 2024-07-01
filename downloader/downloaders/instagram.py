from typing import List
import instaloader
from concurrent.futures import ThreadPoolExecutor
from downloader.status_manager import StatusManager
from downloader.utils import create_save_directory


class InstagramDownloader:
    def __init__(self, save_dir: str, manager: StatusManager, max_workers: int = 5):
        self.save_dir = save_dir
        self.manager = manager
        self.max_workers = max_workers
        self.loader = instaloader.Instaloader(dirname_pattern=self.save_dir)

    def download_post(self, url: str) -> str:
        try:
            post = instaloader.Post.from_shortcode(
                self.loader.context, url.split('/')[-2]
            )
            path_dir = create_save_directory(self.save_dir)
            self.loader.download_post(post, target=path_dir)
            print(f"Downloaded Instagram post {post.shortcode} successfully.")
            description = post.caption[:10] if post.caption else 'No Description'
            return description
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")
            return None

    def download_posts(self, urls: List[str]) -> None:
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for instagram_url in urls:
                executor.submit(
                    self._download_and_update_status, instagram_url)
        print("All Instagram posts downloaded successfully.")

    def _download_and_update_status(self, url: str) -> None:
        description = self.download_post(url)
        if description:
            self.manager.update_status(url, description, 'Completed')
        else:
            self.manager.update_status(url, description, 'Failed')
