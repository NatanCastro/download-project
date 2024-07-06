import { DownloaderFactory } from '../downloaders/downloader_factory'
import { FileDownloader } from '../downloaders/files'
import { YouTubeDownloader } from '../downloaders/youtube'
import { StatusManager } from './status_manager'

type UrlList = string[]

class DownloadManager {
  statusManager: StatusManager
  private fileDownloader: FileDownloader
  private youtubeDownloader: YouTubeDownloader
  private fileUrls: UrlList
  private youtubeUrls: UrlList

  constructor(factory: DownloaderFactory) {
    this.statusManager = new StatusManager()
    this.fileDownloader = factory.createFileDownloader('files', this.statusManager)
    this.youtubeDownloader = factory.createYouTubeDownloader('youtube_videos', this.statusManager)
    this.fileUrls = []
    this.youtubeUrls = []
  }

  private urlType(url: string): 'youtube' | 'file' {
    if (url.includes('youtube') || url.includes('youtu.be')) {
      return 'youtube'
    }

    return 'file'
  }

  addUrl(url: string): void {
    const urlType = this.urlType(url)

    switch (urlType) {
      case 'youtube':
        this.youtubeUrls.push(url)
        this.statusManager.updateStatus(url, 'Pending')

        break

      default:
        this.fileUrls.push(url)
        this.statusManager.updateStatus(url, 'Pending')
        break
    }
  }

  addUrls(urls: string[]): void {
    urls.forEach((u) => this.addUrl(u))
  }

  removeDownload(url: string): void {
    this.fileUrls = this.fileUrls.filter((fileUrl) => fileUrl !== url)
    this.youtubeUrls = this.youtubeUrls.filter((youtubeUrl) => youtubeUrl !== url)
    this.statusManager.removeStatus(url)
  }

  updateStatus(url: string, status: string): void {
    this.statusManager.updateStatus(url, status)
  }

  async downloadAll(): Promise<void> {
    if (this.fileUrls.length > 0) {
      await this.fileDownloader.downloadFiles(this.fileUrls)
    }
    if (this.youtubeUrls.length > 0) {
      await this.youtubeDownloader.downloadVideos(this.youtubeUrls)
    }
  }
}

export { DownloadManager }
