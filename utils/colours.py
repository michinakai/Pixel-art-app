from PIL import Image

palette = []

colour_palette = Image.open('resurrect-64-1x.png')
rgb_palette = colour_palette.convert('RGB')
palette_w = colour_palette.width
x = 0

for i in range(palette_w):
    r, g, b = rgb_palette.getpixel((x, 0))
    x = x + 1
    palette.append([r, g, b])

#print(palette[1][2])




