import os
import random

import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound

WINDOW_TITLE = "My Wardrobe"
WINDOW_HEIGHT = 220
WINDOW_WIDTH = 500
IMG_WIDTH = 250
IMG_HEIGHT = 250
SOUND_EFFECT_FILE_PATH = ""

#store all Tops into a file and skip hidden files
ALL_TOPS = [str('tops/') + imagefile for imagefile in os.listdir('tops/') if not imagefile.startswith('.')]
ALL_BOTTOMS = [str('bottoms/') + imagefile for imagefile in os.listdir('bottoms/') if not imagefile.startswith('.')]

class WardrobeApp:
    def __init__(self, root):
        self.root = root

        #show top/bottom image in the window
        self.top_images = ALL_TOPS
        self.bottom_images = ALL_BOTTOMS

        #save single top & bottom - image filepath
        self.top_image_path = self.top_images[0]
        self.bottom_image_path = self.bottom_images[0]
        
        #create and add top image into Frame
        self.tops_frame = tk.Frame(self.root)
        self.top_image_label = self.create_photo(self.top_image_path, self.tops_frame)

        self.bottoms_frame = tk.Frame(self.root)
        self.bottom_image_label = self.create_photo(self.bottom_image_path, self.bottoms_frame)

        #add top to pack
        self.top_image_label.pack(side=tk.TOP)
        self.bottom_image_label.pack(side=tk.TOP)
        
        self.create_background()


    def create_background(self):
        #add title to window
        self.root.title(WINDOW_TITLE)
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')

        #add all buttons
        self.create_buttons()

        #add clothing
        self.tops_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.bottoms_frame.pack(fill=tk.BOTH, expand=tk.YES)

    def create_buttons(self):
        create_outfit_button = tk.Button(self.bottoms_frame, text="CREATE OUTFIT", command=self.create_outfit)
        create_outfit_button.pack(side=tk.LEFT)

        top_prev_button = tk.Button(self.tops_frame, text="Prev", command=self.get_prev_top)
        top_prev_button.pack(side=tk.LEFT)

        top_next_button = tk.Button(self.tops_frame, text="Next", command=self.get_next_top)
        top_next_button.pack(side=tk.RIGHT)

        bottom_prev_button = tk.Button(self.bottoms_frame, text="Prev", command=self.get_prev_bottom)
        bottom_prev_button.pack(side=tk.LEFT)

        bottom_next_button = tk.Button(self.bottoms_frame, text="Next", command=self.get_next_bottom)
        bottom_next_button.pack(side=tk.RIGHT)

        

    def _get_next_item(self, current_item, category, increment = True):
        #function to move front and back using buttons
        item_index = category.index(current_item)
        final_index = len(category)-1
        next_index = 0

        #increment and at the end of the list
        if increment and item_index==final_index:
            next_index = 0
        #decrement and at the beginning of the list
        elif not increment and item_index==0:
            next_index = final_index
        else:
            incrementor = 1 if increment else -1
            next_index = item_index + incrementor

        next_image = category[next_index]

        #reset and update image based on next_image path
        if current_item in self.top_images:
            image_label = self.top_image_label
            self.top_image_path = next_image
        else:
            image_label = self.bottom_image_label
            self.bottom_image_path = next_image

        #use update func to change image
        self.update_image(next_image, image_label)
    
    def update_image(self, new_image_path, image_label):
        #collect and change image into tk photo obj
        image_file = Image.open(new_image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)

        #update label
        image_label.configure(image=tk_photo)

        image_label.image = tk_photo

    def get_next_top(self):
        self._get_next_item(self.top_image_path, self.top_images, increment=True)

    def get_prev_top(self):
        self._get_next_item(self.top_image_path, self.top_images, increment=False)

    def get_next_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=True)

    def get_prev_bottom(self):
        self._get_next_item(self.bottom_image_path, self.bottom_images, increment=False)

        
    def create_photo(self, image_path, frame):
        image_file = Image.open(image_path)
        image_resized = image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        tk_photo = ImageTk.PhotoImage(image_resized)
        image_label = tk.Label(frame, image=tk_photo, anchor=tk.CENTER)

        image_label.image = tk_photo

        return image_label

    def create_outfit(self):
        #random select top and bottom index
        new_top_index = random.randint(0, len(self.top_images)-1)
        new_bottom_index = random.randint(0, len(self.bottom_images)-1)

        #add clothes onto screen
        self.update_image(self.top_images[new_top_index], self.top_image_label)
        self.update_image(self.bottom_images[new_bottom_index], self.bottom_image_label)

        #add noise
        #playsound(SOUND_EFFECT_FILE_PATH)



root = tk.Tk()
app = WardrobeApp(root)
root.mainloop()