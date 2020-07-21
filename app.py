import os

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500

#store all Tops into a file and skip hidden files
ALL_TOPS = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not file.startswith('.')]

class WardrobeApp:
    def __init__(self, root):
        self.root = root

        #show top image in the window
        self.top_images = ALL_TOPS

        self.create_background()


    def create_background(self):
        #add title to window
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()