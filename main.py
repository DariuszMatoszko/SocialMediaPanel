import tkinter as tk
import webbrowser

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
