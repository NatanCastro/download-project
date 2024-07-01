import tkinter as tk
from downloader.manager import DownloadManager
from downloader.downloader_factory import DownloaderFactory
from downloader.utils import remove_query_params
from custom_tk.colored_listbox import ColoredListbox
from utils.colors import colors


class DownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Downloader")
        self.root.configure(bg="#2b2b2b")

        self.factory = DownloaderFactory()
        self.manager = DownloadManager(self.factory)

        # URL Listbox (Sidebar)
        self.sidebar_frame = tk.Frame(root, bg="#333333")
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsw")

        self.url_listbox_label = tk.Label(
            self.sidebar_frame, text="URL List", bg="#333333", fg="white")
        self.url_listbox_label.pack(padx=10, pady=(10, 0))

        self.url_listbox = tk.Listbox(
            self.sidebar_frame, width=50, height=20, bg="#444444", fg="white")
        self.url_listbox.pack(padx=10, pady=10)

        self.remove_button = tk.Button(
            self.sidebar_frame, text="Remove", command=self.remove_url)
        self.remove_button.pack(pady=10)

        self.url_entry = tk.Entry(
            self.sidebar_frame, width=50, bg="#555555", fg="white")
        self.url_entry.pack(padx=10, pady=(0, 10))
        self.url_entry.bind("<Return>", self.add_url)

        self.add_button = tk.Button(
            self.sidebar_frame, text="Add URL", command=self.add_url)
        self.add_button.pack(pady=10)

        self.download_button = tk.Button(
            self.sidebar_frame, text="Download", command=self.start_download)
        self.download_button.pack(pady=10)

        # Status Listbox (New)
        self.status_frame = tk.Frame(root, bg="#333333")
        self.status_frame.grid(row=0, column=1, rowspan=4, sticky="nse")

        self.status_listbox_label = tk.Label(
            self.status_frame, text="Download Status", bg="#333333", fg="white")
        self.status_listbox_label.pack(padx=10, pady=(10, 0))

        self.status_listbox = ColoredListbox(
            self.status_frame, width=50, height=20, bg="#444444", fg="white")
        self.status_listbox.pack(padx=10, pady=10)

    def add_url(self, event=None):
        url = self.url_entry.get()
        if url:
            self.url_listbox.insert(tk.END, url)
            if "youtube.com" in url or "youtu.be" in url:
                self.manager.add_youtube_url(url)
            elif "instagram.com" in url:
                self.manager.add_instagram_url(url)
            else:
                url = remove_query_params(url)
                self.manager.add_file_url(url)
            self.url_entry.delete(0, tk.END)
            self.update_status_listbox()

    def remove_url(self):
        selected_url = self.url_listbox.get(tk.ACTIVE)
        self.url_listbox.delete(tk.ACTIVE)
        self.manager.remove_download(selected_url)
        self.update_status_listbox()

    def start_download(self):
        self.update_status_listbox()
        self.manager.download_all()

    def update_status_listbox(self):
        self.status_listbox.delete(0, tk.END)
        for url, status in self.manager.status_manager.status.items():
            self.status_listbox.insert(tk.END, status)
            index = self.status_listbox.size() - 1
            if 'Downloading' in status:
                self.status_listbox.set_item_color(index, colors['YELLOW'])
            elif 'Completed' in status:
                self.status_listbox.set_item_color(index, colors['GREEN'])
            elif 'Failed' in status:
                self.status_listbox.set_item_color(index, colors['RED'])
            else:
                self.status_listbox.set_item_color(index, colors['WHITE'])


if __name__ == "__main__":
    root = tk.Tk()
    app = DownloaderGUI(root)
    root.mainloop()
