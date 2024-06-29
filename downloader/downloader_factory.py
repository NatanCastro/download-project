from downloader.downloaders.files import FileDownloader, FileDownloaderBase
from downloader.downloaders.youtube import YouTubeDownloader, YouTubeDownloaderBase
from downloader.downloaders.instagram import InstagramDownloader, InstagramDownloaderBase


class DownloaderFactory:
    @staticmethod
    def create_file_downloader(save_dir: str, max_workers: int = 5) -> FileDownloaderBase:
        return FileDownloader(save_dir=save_dir, max_workers=max_workers)

    @staticmethod
    def create_youtube_downloader(save_dir: str, max_workers: int = 5) -> YouTubeDownloaderBase:
        return YouTubeDownloader(save_dir=save_dir, max_workers=max_workers)

    @staticmethod
    def create_instagram_downloader(save_dir: str, max_workers: int = 5) -> InstagramDownloaderBase:
        return InstagramDownloader(save_dir=save_dir, max_workers=max_workers)
