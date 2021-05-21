#!/usr/bin/env python3
from PIL import Image
import os

list_dir = os.listdir()
print(list_dir)
for directory in list_dir:
    if directory == "resize_image.py":
        continue
    list_files = os.listdir(directory)
    if not os.path.exists(f"{directory}/low_size"):
        os.mkdir(f"{directory}/low_size")
        print(list_files)
        for image_file in list_files:
            img = Image.open(f"{directory}/{image_file}")
            width, height = img.size
            img = img.resize((int(width/6), int(height/6)), Image.ANTIALIAS)
            img.save(f"{directory}/low_size/resized_{image_file}")
