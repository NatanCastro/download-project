import * as fs from 'fs'
import * as path from 'path'
import axios from 'axios'
import { createSaveDirectory, getFileExtension, getSubDirectory } from '../utils'
import { StatusManager } from '../managers/status_manager'

// Define the type for the URL list
type UrlList = string[]

// FileDownloader class
class FileDownloader {
  saveDir: string
  manager: StatusManager
  maxWorkers: number

  constructor(saveDir: string, manager: StatusManager, maxWorkers: number = 5) {
    this.saveDir = saveDir
    this.manager = manager
    this.maxWorkers = maxWorkers
  }

  async downloadFile(url: string): Promise<string | null> {
    try {
      const response = await axios.get(url, { responseType: 'arraybuffer' })
      const fileExtension = getFileExtension(url)
      const subDir = getSubDirectory(fileExtension)
      const dirPath = createSaveDirectory(this.saveDir, subDir)
      const fileName = path.basename(url)
      const filePath = path.join(dirPath, fileName)
      fs.writeFileSync(filePath, response.data)
      console.log(`Downloaded ${fileName} successfully to ${subDir}`)
      return fileName
    } catch (error) {
      console.error(`Failed to download ${url}. Error: ${error}`)
      return null
    }
  }

  async downloadFiles(urls: UrlList): Promise<void> {
    const promises = urls.map((url) => this._downloadAndUpdateStatus(url))
    await Promise.all(promises)
    console.log('All files downloaded successfully.')
  }

  private async _downloadAndUpdateStatus(url: string): Promise<void> {
    const fileName = await this.downloadFile(url)
    if (fileName) {
      this.manager.updateStatus(url, 'Completed')
    } else {
      this.manager.updateStatus(url, 'Failed')
    }
  }
}

export { FileDownloader }
