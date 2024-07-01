from typing import List
from pytube import YouTube
from concurrent.futures import ThreadPoolExecutor
from downloader.utils import create_save_directory
from downloader.status_manager import StatusManager


class YouTubeDownloader:
    def __init__(self, save_dir: str, manager: StatusManager, max_workers: int = 5):
        self.save_dir = save_dir
        self.manager = manager
        self.max_workers = max_workers

    def download_video(self, url: str) -> str:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            dir_path = create_save_directory(self.save_dir)
            file_path = stream.download(output_path=dir_path)
            print(f"Downloaded {yt.title} successfully to {file_path}")
            return yt.title
        except Exception as e:
            print(f"Failed to download {url}. Error: {e}")
            return None

    def download_videos(self, urls: List[str]) -> None:
        create_save_directory(self.save_dir)
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            for youtube_url in urls:
                executor.submit(
                    self._download_and_update_status, youtube_url)
        print("All YouTube videos downloaded successfully.")

    def _download_and_update_status(self, url: str) -> None:
        video_title = self.download_video(url)
        if video_title:
            self.manager.update_status(url, video_title, 'Completed')
        else:
            self.manager.update_status(url, video_title, 'Failed')
