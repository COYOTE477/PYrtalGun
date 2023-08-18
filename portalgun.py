from PIL import Image
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
color1 = config['colors']['color1']
color2 = config['colors']['color2']

main_image = Image.open("main.jpg")
mask1 = Image.open("mask1.jpg").convert("L")
mask2 = Image.open("mask2.jpg").convert("L")
# Define color
maincolor_hex = color1
stripe_hex = color2

# Convert hex color codes to RGB tuples
maincolor = (int(maincolor_hex[1:3], 16), int(maincolor_hex[3:5], 16), int(maincolor_hex[5:7], 16))
stripe = (int(stripe_hex[1:3], 16), int(stripe_hex[3:5], 16), int(stripe_hex[5:7], 16))

# Iterate over pixels
width, height = main_image.size
for x in range(width):
    for y in range(height):
        # Check mask1
        if mask1.getpixel((x, y)) > 128:  # If the mask pixel is more white than black
            main_image.putpixel((x, y), maincolor)
        # Check mask2
        elif mask2.getpixel((x, y)) > 128:  
            main_image.putpixel((x, y), stripe)

main_image = main_image.convert("RGBA")
main_image.save("result.png")
os.system("VTFCmd -file result.png")


