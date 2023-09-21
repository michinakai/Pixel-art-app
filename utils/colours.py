import os
import keyboard
from PIL import Image

path = r"C:\Users\nakaim\Documents\GitHub\Pixel-art\palettes"
palette_list = os.listdir(path)
palette = []

palette_num = 0

colour_palette = Image.open(f"palettes/{palette_list[palette_num]}")
rgb_palette = colour_palette.convert('RGB')
palette_w = colour_palette.width

def colour_list():
    x = 0

    for i in range(palette_w):
        r, g, b = rgb_palette.getpixel((x, 0))
        x = x + 1
        palette.append([r, g, b])
        
colour_list()





