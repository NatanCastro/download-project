import * as path from 'path'
import * as fs from 'fs'
import ytdl from 'ytdl-core'
import { createSaveDirectory } from '../utils'
import { StatusManager } from '../managers/status_manager'

// Define the type for the URL list
type UrlList = string[]

// YouTubeDownloader class
class YouTubeDownloader {
  saveDir: string
  manager: StatusManager
  maxWorkers: number

  constructor(saveDir: string, manager: StatusManager, maxWorkers: number = 5) {
    this.saveDir = saveDir
    this.manager = manager
    this.maxWorkers = maxWorkers
  }

  async downloadVideo(url: string): Promise<string | null> {
    try {
      this.manager.updateStatus(url, 'Downloading')
      const info = await ytdl.getInfo(url)
      const videoTitle = info.videoDetails.title
      const dirPath = createSaveDirectory(this.saveDir)
      const filePath = path.join(dirPath, `${videoTitle}.mp4`)

      const videoStream = ytdl(url, { quality: 'highest' })
      const fileStream = fs.createWriteStream(filePath)

      videoStream.pipe(fileStream)

      return new Promise((resolve, reject) => {
        fileStream.on('finish', () => {
          console.log(`Downloaded ${videoTitle} successfully to ${filePath}`)
          resolve(videoTitle)
        })

        fileStream.on('error', (error) => {
          console.error(`Failed to download ${url}. Error: ${error}`)
          reject(null)
        })
      })
    } catch (error) {
      console.error(`Failed to download ${url}. Error: ${error}`)
      return null
    }
  }

  async downloadVideos(urls: UrlList): Promise<void> {
    createSaveDirectory(this.saveDir)
    const promises = urls.map((url) => this.downloadAndUpdateStatus(url))
    await Promise.all(promises)
    console.log('All YouTube videos downloaded successfully.')
  }

  private async downloadAndUpdateStatus(url: string): Promise<void> {
    const videoTitle = await this.downloadVideo(url)
    if (videoTitle) {
      this.manager.updateStatus(url, 'Completed')
    } else {
      this.manager.updateStatus(url, 'Failed')
    }
  }
}

export { YouTubeDownloader }
