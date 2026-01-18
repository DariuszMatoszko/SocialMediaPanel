import tkinter as tk
import webbrowser
import os
import subprocess

BACKGROUND_COLOR = "#1f1f1f"
BUTTON_COLOR = "#2f2f2f"
BUTTON_TEXT_COLOR = "#f5f5f5"
HEADER_COLOR = "#ffffff"
SUBHEADER_COLOR = "#efefef"

root = tk.Tk()
root.title("GEOINVEST - SOCIAL_MEDIA_MACRO")
root.configure(bg=BACKGROUND_COLOR)
root.resizable(False, False)

header_label = tk.Label(root, text="GEOINVEST", bg=BACKGROUND_COLOR, fg=HEADER_COLOR)
header_label.config(font=("Arial", 18, "bold"))
header_label.pack(pady=(10, 0))

subheader_label = tk.Label(root, text="SOCIAL_MEDIA_MACRO", bg=BACKGROUND_COLOR, fg=SUBHEADER_COLOR)
subheader_label.config(font=("Arial", 12))
subheader_label.pack(pady=(0, 10))

button_fb = tk.Button(root, text="Facebook", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                      activebackground=BUTTON_COLOR, activeforeground=BUTTON_TEXT_COLOR,
                      command=lambda: webbrowser.open("https://www.facebook.com/GEOINVEST"))
button_fb.pack(pady=2)

button_ig = tk.Button(root, text="Instagram", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                      activebackground=BUTTON_COLOR, activeforeground=BUTTON_TEXT_COLOR,
                      command=lambda: webbrowser.open("https://business.facebook.com/creatorstudio"))
button_ig.pack(pady=2)

button_tt = tk.Button(root, text="TikTok", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                      activebackground=BUTTON_COLOR, activeforeground=BUTTON_TEXT_COLOR,
                      command=lambda: webbrowser.open("https://www.tiktok.com/business/en"))
button_tt.pack(pady=2)

button_x = tk.Button(root, text="X", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                     activebackground=BUTTON_COLOR, activeforeground=BUTTON_TEXT_COLOR,
                     command=lambda: webbrowser.open("https://x.com/GEOINVEST"))
button_x.pack(pady=2)

def adjust_transparency(value):
    alpha = float(value) / 100.0
    root.attributes("-alpha", alpha)

slider = tk.Scale(root, from_=10, to=90, orient=tk.HORIZONTAL, command=adjust_transparency,
                  bg=BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR, highlightthickness=0, bd=0,
                  troughcolor=BUTTON_COLOR, activebackground=BUTTON_COLOR)
slider.pack(side=tk.BOTTOM, fill=tk.X)
slider.set(90)

root.mainloop()
class SocialPanel:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Social Media Panel")
        self.root.configure(bg=BACKGROUND_COLOR)
        self.root.resizable(False, False)
        self.root.attributes("-alpha", 0.9)

        header_label = tk.Label(self.root, text="GEOINVEST", fg=HEADER_COLOR, bg=BACKGROUND_COLOR, font=("Arial", 16, "bold"))
        subheader_label = tk.Label(self.root, text="SOCIAL_MEDIA_MACRO", fg=SUBHEADER_COLOR, bg=BACKGROUND_COLOR, font=("Arial", 12))
        header_label.pack(pady=(10, 0))
        subheader_label.pack(pady=(0, 15))

        platforms = [
            {"name": "Facebook", "url": "https://www.facebook.com/login", "file": "facebook.txt"},
            {"name": "Instagram", "url": "https://www.instagram.com/accounts/login/", "file": "instagram.txt"},
            {"name": "TikTok", "url": "https://www.tiktok.com/login", "file": "tiktok.txt"},
            {"name": "X", "url": "https://x.com/i/flow/login", "file": "x.txt"}
        ]

        for platform in platforms:
            frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)

            btn_platform = tk.Button(frame, text=platform["name"], bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                     relief=tk.FLAT, width=14, height=2,
                                     command=lambda url=platform["url"]: webbrowser.open(url))
            btn_platform.pack(side="left", padx=5, pady=5)

            btn_data = tk.Button(frame, text="Otwórz dane", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR,
                                 relief=tk.FLAT, command=lambda file=platform["file"]: self.open_file(file))
            btn_data.pack(side="left", padx=5, pady=5)

            frame.pack(pady=5)

        slider_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        slider_label = tk.Label(slider_frame, text="Przezroczystość:", fg=SUBHEADER_COLOR, bg=BACKGROUND_COLOR)
        slider_label.pack(side="left", padx=(5, 5))

        opacity_slider = tk.Scale(slider_frame, from_=10, to=90, orient=tk.HORIZONTAL,
                                  bg=BACKGROUND_COLOR, fg=BUTTON_TEXT_COLOR,
                                  highlightthickness=0, troughcolor=BUTTON_COLOR,
                                  command=self._change_opacity)
        opacity_slider.set(90)
        opacity_slider.pack(side="left", padx=(0, 5))
        slider_frame.pack(pady=(10, 10))

    def open_file(self, filename):
        try:
            base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
            filepath = os.path.join(base_path, filename)
            subprocess.Popen(["notepad.exe", filepath])
        except Exception as e:
            print(f"Błąd otwierania pliku: {e}")

    def _change_opacity(self, value):
        try:
            opacity = float(value) / 100.0
        except Exception:
            opacity = 0.9
        self.root.attributes("-alpha", opacity)

    def run(self):
        self.root.mainloop()

def main():
    panel = SocialPanel()
    panel.run()

if __name__ == "__main__":
    main()
