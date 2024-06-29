import tkinter as tk
from tkinter import messagebox
from downloader.manager import DownloadManager
from downloader.downloader_factory import DownloaderFactory
from downloader.utils import remove_query_params


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
            self.sidebar_frame,
            text="Remove Selected URL",
            command=self.remove_selected_url,
            bg="#ff5555", fg="white"
        )
        self.remove_button.pack(padx=10, pady=(0, 10))

        # URL Entry and Controls
        self.main_frame = tk.Frame(root, bg="#2b2b2b")
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.url_label = tk.Label(
            self.main_frame, text="Enter URL:", bg="#2b2b2b", fg="white")
        self.url_label.grid(row=0, column=0, sticky="w")

        self.url_entry = tk.Entry(
            self.main_frame, width=50, bg="#444444", fg="white")
        self.url_entry.grid(row=1, column=0, pady=(0, 10))

        self.add_button = tk.Button(
            self.main_frame,
            text="Add URL",
            command=self.add_url,
            bg="#5fba7d",
            fg="white"
        )
        self.add_button.grid(row=2, column=0, pady=(0, 10))

        self.download_button = tk.Button(
            self.main_frame,
            text="Download All",
            command=self.download_all,
            bg="#5fba7d",
            fg="white"
        )
        self.download_button.grid(row=3, column=0, pady=(0, 10))

    def add_url(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a URL")
            return
        self.url_listbox.insert(tk.END, url)
        self.url_entry.delete(0, tk.END)

    def remove_selected_url(self):
        selected_indices = self.url_listbox.curselection()
        for index in selected_indices[::-1]:
            self.url_listbox.delete(index)

    def download_all(self):
        urls = self.url_listbox.get(0, tk.END)
        if not urls:
            messagebox.showerror("Error", "No URLs to download")
            return

        try:
            for url in urls:
                self.add_url_to_manager(url)
            self.manager.download_all()
            messagebox.showinfo("Success", "Download started")
            self.url_listbox.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_url_to_manager(self, url: str):
        if "youtube.com" in url or "youtu.be" in url:
            self.manager.add_youtube_url(url)
        elif "instagram.com" in url:
            self.manager.add_instagram_url(url)
        else:
            self.manager.add_file_url(remove_query_params(url))


if __name__ == "__main__":
    root = tk.Tk()
    app = DownloaderGUI(root)
    root.mainloop()
