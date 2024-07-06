// Define the video file extensions
const VIDEO_FILE_EXTENSIONS: Set<string> = new Set([
  '.mp4',
  '.mkv',
  '.avi',
  '.mov',
  '.flv',
  '.wmv',
  '.webm',
  '.mpeg',
  '.mpg',
  '.3gp',
  '.m4v',
  '.ts',
  '.vob',
  '.m2ts',
  '.mts'
])

// Define the image file extensions
const IMAGE_FILE_EXTENSIONS: Set<string> = new Set([
  '.jpg',
  '.jpeg',
  '.png',
  '.gif',
  '.bmp',
  '.tiff',
  '.tif',
  '.svg',
  '.webp',
  '.ico',
  '.psd',
  '.ai',
  '.eps',
  '.raw',
  '.cr2',
  '.nef',
  '.orf',
  '.arw',
  '.dng'
])

// Define the base directory path
const BASE_DIR_PATH: string = require('os').homedir() + '/Documents/downloader'

// Export the constants
export { VIDEO_FILE_EXTENSIONS, IMAGE_FILE_EXTENSIONS, BASE_DIR_PATH }
