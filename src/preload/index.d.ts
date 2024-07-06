import { ElectronAPI } from '@electron-toolkit/preload'
import { ApiInterface } from './index'

declare global {
  interface Window {
    electron: ElectronAPI
    api: ApiInterface
  }
}
