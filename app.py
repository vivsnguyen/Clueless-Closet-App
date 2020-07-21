import os

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500
IMG_WIDTH = 250
IMG_HEIGHT = 250

#store all Tops into a file and skip hidden files
ALL_TOPS = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self, root):
        self.root = root

        #show top image in the window
        self.top_images = ALL_TOPS

        #save single top - image filepath
        self.top_image_path = self.top_images[0]
        
        #create and add top image into Frame
        self.tops_frame = tk.Frame(self.root)
        self.top_image_label = self.create_photo(self.top_image_path, self.tops_frame)

        #add top to pack
        self.top_image_label.pack(side=tk.TOP)
        
        self.create_background()


    def create_background(self):
        #add title to window
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

        #add all buttons
        self.create_buttons()

        #add clothing
        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        top_prev_button = tk.Button(self.tops_frame, text="Prev")
        top_prev_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame, text="Next")
        top_next_button.pack(side=tk.LEFT)

    def create_photo(self, image_path, frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image=tk_photo, anchor=tk.CENTER)

        image_label.image = tk_photo

        return image_label


root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()