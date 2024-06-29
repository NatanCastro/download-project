from downloader.manager import DownloadManager
from downloader.downloader_factory import DownloaderFactory
from downloader.utils import remove_query_params


def main():
    factory = DownloaderFactory()
    manager = DownloadManager(factory)

    while True:
        url = input("Enter URL (or type 'download' to start downloading): ")
        if url == "download":
            break
        if "youtube.com" in url or "youtu.be" in url:
            manager.add_youtube_url(url)
        elif "instagram.com" in url:
            manager.add_instagram_url(url)
        else:
            manager.add_file_url(remove_query_params(url))

    manager.download_all()


if __name__ == "__main__":
    main()
