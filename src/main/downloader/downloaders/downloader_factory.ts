import { FileDownloader } from './files'
import { YouTubeDownloader } from './youtube'
import { StatusManager } from '../managers/status_manager'

class DownloaderFactory {
  createFileDownloader(saveDir: string, manager: StatusManager): FileDownloader {
    return new FileDownloader(saveDir, manager)
  }

  createYouTubeDownloader(saveDir: string, manager: StatusManager): YouTubeDownloader {
    return new YouTubeDownloader(saveDir, manager)
  }
}

export { DownloaderFactory }
