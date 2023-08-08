from PIL import Image

palette = []

clr_palette = Image.open('sweetie-16-1x.png')
rgb_palette = clr_palette.convert('RGB')
palette_w = clr_palette.width
x = 0

for i in range(palette_w):
    r, g, b = rgb_palette.getpixel((x, 0))
    x = x + 1
    palette.append([r, g, b])

print(palette[1][2])




