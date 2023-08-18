from PIL import Image
import discord
import json
from discord import app_commands

from discord.ext import commands
from discord import File
import os

# Create bot
bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

# Define slash command
@bot.hybrid_command(fallback="get")
async def generate(name="setcolors", description="Sets two colors", options=[
    {
        "name": "color1",
        "description": "Hex code for first color",
        "type": 3,
        "required": True
    },
    {
        "name": "color2",
        "description": "Hex code for second color",
        "type": 3,
        "required": True
    }
]):
    async def setcolors(ctx, color1: str, color2: str):
    # This function is called when the /setcolors command is used
    # Do something with color1 and color2...
        main_image = Image.open("main.jpg")
        mask1 = Image.open("mask1.jpg").convert("L")
        mask2 = Image.open("mask2.jpg").convert("L")
        # Define colors

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
        await ctx.send("Color 1 is {color1} and color 2 is {color2}")
    # Open images
    
# Run bot
bot.run("your-bot-token-here")


