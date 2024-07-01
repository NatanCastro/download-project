from downloader.downloaders.files import FileDownloader
from downloader.downloaders.youtube import YouTubeDownloader
from downloader.downloaders.instagram import InstagramDownloader
from downloader.status_manager import StatusManager


class DownloaderFactory:
    def create_file_downloader(self, save_dir: str, manager: StatusManager) -> FileDownloader:
        return FileDownloader(save_dir=save_dir, manager=manager)

    def create_youtube_downloader(self, save_dir: str, manager: StatusManager) -> YouTubeDownloader:
        return YouTubeDownloader(save_dir=save_dir, manager=manager)

    def create_instagram_downloader(self, save_dir: str, manager: StatusManager) -> InstagramDownloader:
        return InstagramDownloader(save_dir=save_dir, manager=manager)
