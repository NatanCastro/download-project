// Import necessary modules and constants
import * as fs from 'fs'
import * as path from 'path'
import { IMAGE_FILE_EXTENSIONS, VIDEO_FILE_EXTENSIONS, BASE_DIR_PATH } from './config'

// Function to remove query parameters from a URL
function removeQueryParams(url: string): string {
  return url.split('?')[0]
}

// Function to create a save directory
function createSaveDirectory(dir: string, subDir?: string): string {
  const dirPath = subDir ? path.join(BASE_DIR_PATH, dir, subDir) : path.join(BASE_DIR_PATH, dir)
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true })
  }
  return dirPath
}

// Function to get the file extension from a URL
function getFileExtension(url: string): string {
  return path.extname(url).toLowerCase()
}

// Function to get the file type based on the extension
function getFileType(fileExtension: string): string {
  if (VIDEO_FILE_EXTENSIONS.has(fileExtension)) {
    return 'video'
  } else if (IMAGE_FILE_EXTENSIONS.has(fileExtension)) {
    return 'image'
  } else {
    return 'other'
  }
}

// Function to get the sub-directory based on the file type
function getSubDirectory(fileExtension: string): string {
  const fileType = getFileType(fileExtension)

  switch (fileType) {
    case 'video':
      return 'videos'
    case 'image':
      return 'images'
    default:
      return 'others'
  }
}

export { removeQueryParams, createSaveDirectory, getFileExtension, getFileType, getSubDirectory }
