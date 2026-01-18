import os
import subprocess
import tkinter as tk
from tkinter import ttk
import webbrowser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

SOCIALS = [
    {
        "name": "Facebook",
        "file": "facebook.txt",
        "url": "https://www.facebook.com",
    },
    {
        "name": "Instagram",
        "file": "instagram.txt",
        "url": "https://www.instagram.com",
    },
    {
        "name": "TikTok",
        "file": "tiktok.txt",
        "url": "https://www.tiktok.com",
    },
    {
        "name": "X",
        "file": "x.txt",
        "url": "https://www.twitter.com",
    },
]


class SocialPanel:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Panel Social Media")
        self.root.geometry("500x400")
        self.root.attributes("-alpha", 0.9)

        self.build_ui()

    def build_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        for idx, social in enumerate(SOCIALS):
            button = ttk.Button(
                main_frame,
                text=social["name"],
                command=lambda url=social["url"]: self.launch_platform(url),
            )
            button.grid(row=idx, column=0, pady=5, sticky="w")

            note_button = ttk.Button(
                main_frame,
                text="Otwórz dane",
                command=lambda f=social["file"]: self.open_notes(f),
            )
            note_button.grid(row=idx, column=1, padx=10)

    @staticmethod
    def launch_platform(url: str) -> None:
        webbrowser.open(url)

    @staticmethod
    def open_notes(filename: str) -> None:
        filepath = os.path.join(DATA_DIR, filename)
        subprocess.Popen(["notepad.exe", filepath])


if __name__ == "__main__":
    root = tk.Tk()
    app = SocialPanel(root)
    root.mainloop()
