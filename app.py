import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

class WardrobeApp:
    def __init__(self, root):
        self.root = root

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()