import { EventEmitter } from 'events'

class StatusManager extends EventEmitter {
  private status: { [url: string]: string }

  constructor() {
    super()
    this.status = {}
  }

  updateStatus(url: string, status: string): void {
    this.status[url] = status
    this.emit('statusChange', { url, status })
  }

  getStatus(url: string): string {
    return this.status[url] || 'Pending'
  }

  removeStatus(url: string): void {
    delete this.status[url]
    this.emit('statusChange', { url, status: 'Removed' })
  }
}

export { StatusManager }
