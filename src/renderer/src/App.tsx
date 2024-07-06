import Versions from './components/Versions'
import { useEffect, useState } from 'react'

type Status = {
  [arg: string]: string
}

function App(): JSX.Element {
  const [urls, setUrls] = useState<string[]>([])
  const [statuses, setStatuses] = useState<Status>({})
  const [inputUrl, setInputUrl] = useState<string>()

  useEffect(() => {
    window.api.onStatusChange((status) => {
      setStatuses((prevStatuses) => ({
        ...prevStatuses,
        [status.url]: status.status
      }))
    })
  }, [])

  const handleAddUrl = (): void => {
    if (inputUrl) {
      window.api.addUrl(inputUrl)
      setUrls([...urls, inputUrl])
      setStatuses({ ...statuses, [inputUrl]: 'Pending' })
      setInputUrl('')
    }
  }

  const handleRemoveUrl = (url: string): void => {
    window.api.removeUrl(url)
    setUrls(urls.filter((item) => item !== url))
    setStatuses((prev) => {
      const { [url]: _, ...newStatuses } = prev
      return newStatuses
    })
  }

  const handleDownloadAll = (): void => {
    window.api.downloadAll()
  }

  return (
    <>
      <div className="flex bg-gray-900 text-white h-screen">
        <div className="w-1/3 bg-gray-800 p-4">
          <h2 className="text-xl mb-4">URL List</h2>
          <ul className="mb-4">
            {urls.map((url) => (
              <li key={url} className="flex justify-between items-center mb-2">
                {url}
                <button
                  className="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-2 rounded"
                  onClick={() => handleRemoveUrl(url)}
                >
                  Remove
                </button>
              </li>
            ))}
          </ul>
          <input
            type="text"
            value={inputUrl}
            onChange={(e) => setInputUrl(e.target.value)}
            placeholder="Enter URL"
            className="w-full p-2 mb-2 bg-gray-700 text-white rounded"
          />
          <button
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-2 w-full"
            onClick={handleAddUrl}
          >
            Add URL
          </button>
          <button
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-full"
            onClick={handleDownloadAll}
          >
            Download All
          </button>
        </div>
        <div className="w-2/3 bg-gray-700 p-4">
          <h2 className="text-xl mb-4">Download Status</h2>
          <ul>
            {Object.entries(statuses).map(([url, status]) => {
              const backgroundColor = getStatusColor(status)
              const color = backgroundColor === 'green' ? 'white' : 'black'
              return (
                <li key={url} className="mb-2" style={{ backgroundColor, color }}>
                  {url} - {status}
                </li>
              )
            })}
          </ul>
        </div>
      </div>
      <Versions></Versions>
    </>
  )
}
const getStatusColor = (status: string): string => {
  if (status.includes('Downloading')) return 'yellow'
  if (status.includes('Completed')) return 'green'
  if (status.includes('Failed')) return 'red'
  return 'white'
}

export default App
