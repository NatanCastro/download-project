from typing import Dict


class StatusManager:
    def __init__(self):
        self.status: Dict[str, str] = {}

    def update_status(self, url: str, status: str) -> None:
        self.status[url] = status

    def get_status(self, url: str) -> str:
        return self.status.get(url, 'Pending')

    def remove_status(self, url: str) -> None:
        if url in self.status:
            del self.status[url]
