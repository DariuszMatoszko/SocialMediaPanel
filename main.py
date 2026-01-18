import os
import subprocess
import tkinter as tk
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

BACKGROUND_COLOR = "#1f1f1f"
BUTTON_COLOR = "#2f2f2f"
BUTTON_TEXT_COLOR = "#f5f5f5"
HEADER_COLOR = "#ffffff"
SUBHEADER_COLOR = "#cfcfcf"

DEFAULT_ALPHA = 0.95
MIN_ALPHA_PERCENT = 10
MAX_ALPHA_PERCENT = 90


class SocialPanel:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Panel Social Media")
        self.root.geometry("340x380")
        self.root.configure(bg=BACKGROUND_COLOR)
        self.root.attributes("-alpha", DEFAULT_ALPHA)

        self.build_ui()

    def build_ui(self) -> None:
        main_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        main_frame.pack(fill=tk.BOTH, expand=True)

        content_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
        content_frame.pack(expand=True)

        header_label = tk.Label(
            content_frame,
            text="GEOINVEST",
            font=("Segoe UI", 20, "bold"),
            fg=HEADER_COLOR,
            bg=BACKGROUND_COLOR,
        )
        header_label.pack(pady=(10, 4))

        subheader_label = tk.Label(
            content_frame,
            text="SOCIAL_MEDIA_MACRO",
            font=("Segoe UI", 12, "bold"),
            fg=SUBHEADER_COLOR,
            bg=BACKGROUND_COLOR,
        )
        subheader_label.pack(pady=(0, 16))

        buttons_frame = tk.Frame(content_frame, bg=BACKGROUND_COLOR)
        buttons_frame.pack()

        for idx, social in enumerate(SOCIALS):
            platform_button = tk.Button(
                buttons_frame,
                text=social["name"],
                command=lambda url=social["url"]: self.launch_platform(url),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                activebackground=BUTTON_COLOR,
                activeforeground=BUTTON_TEXT_COLOR,
                relief=tk.FLAT,
                bd=0,
                height=2,
                width=14,
            )
            platform_button.grid(
                row=idx,
                column=0,
                padx=(0, 8),
                pady=6,
            )

            note_button = tk.Button(
                buttons_frame,
                text="Otwórz dane",
                command=lambda f=social["file"]: self.open_notes(f),
                bg=BUTTON_COLOR,
                fg=BUTTON_TEXT_COLOR,
                activebackground=BUTTON_COLOR,
                activeforeground=BUTTON_TEXT_COLOR,
                relief=tk.FLAT,
                bd=0,
                height=2,
                width=14,
            )
            note_button.grid(
                row=idx,
                column=1,
                padx=(8, 0),
                pady=6,
            )

        slider_frame = tk.Frame(main_frame, bg=BACKGROUND_COLOR)
        slider_frame.pack(fill=tk.X, padx=24, pady=(10, 16))

        slider_label = tk.Label(
            slider_frame,
            text="Przezroczystość panelu",
            font=("Segoe UI", 10, "bold"),
            fg=SUBHEADER_COLOR,
            bg=BACKGROUND_COLOR,
        )
        slider_label.pack(anchor="w")

        self.opacity_scale = tk.Scale(
            slider_frame,
            from_=MIN_ALPHA_PERCENT,
            to=MAX_ALPHA_PERCENT,
            orient=tk.HORIZONTAL,
            length=240,
            bg=BACKGROUND_COLOR,
            fg=SUBHEADER_COLOR,
            highlightthickness=0,
            troughcolor=BUTTON_COLOR,
            activebackground=BUTTON_COLOR,
            command=self.update_opacity,
        )
        self.opacity_scale.set(MAX_ALPHA_PERCENT)
        self.opacity_scale.pack(fill=tk.X, pady=(6, 0))

    @staticmethod
    def launch_platform(url: str) -> None:
        webbrowser.open(url)

    @staticmethod
    def open_notes(filename: str) -> None:
        filepath = os.path.join(DATA_DIR, filename)
        subprocess.Popen(["notepad.exe", filepath])

    def update_opacity(self, value: str) -> None:
        try:
            percent = float(value)
        except ValueError:
            return
        self.root.attributes("-alpha", percent / 100)


if __name__ == "__main__":
    root = tk.Tk()
    app = SocialPanel(root)
    root.mainloop()
