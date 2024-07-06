import { contextBridge, ipcRenderer } from 'electron'
import { electronAPI } from '@electron-toolkit/preload'

type Status = {
  url: string
  status: string
}

export interface ApiInterface {
  addUrl: (url: string) => Promise<void>
  downloadAll: () => Promise<void>
  removeUrl: (url: string) => Promise<void>
  onStatusChange: (callback: (status: Status) => void) => void
}

// Custom APIs for renderer
const api: ApiInterface = {
  addUrl: (url) => ipcRenderer.invoke('addUrl', url),
  downloadAll: () => ipcRenderer.invoke('downloadAll'),
  removeUrl: (url) => ipcRenderer.invoke('removeUrl', url),
  onStatusChange: (callback) => {
    ipcRenderer.on('statusChange', (_, status) => callback(status))
  }
}

// Use `contextBridge` APIs to expose Electron APIs to
// renderer only if context isolation is enabled, otherwise
// just add to the DOM global.
if (process.contextIsolated) {
  try {
    contextBridge.exposeInMainWorld('electron', electronAPI)
    contextBridge.exposeInMainWorld('api', api)
  } catch (error) {
    console.error(error)
  }
} else {
  // @ts-ignore (define in dts)
  window.electron = electronAPI
  // @ts-ignore (define in dts)
  window.api = api
}
