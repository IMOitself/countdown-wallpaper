from PIL import Image, ImageDraw, ImageFont
import ctypes
import os
from datetime import datetime

script_directory = os.path.dirname(os.path.abspath(__file__))
input_image_path = os.path.join(script_directory, "wallpaper.jpg") 
output_image_path = os.path.join(script_directory, "wallpaper_with_text.png")

days_left = (datetime(2025, 11, 29) - datetime.now()).days
my_text = f"{days_left} days left"
text_xy_offset = (00, 250) 
font_path = "font.ttf" 
font_size = 30


try:
    image = Image.open(input_image_path)
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype(font_path, font_size)

    img_width, img_height = image.size
    
    bbox = draw.textbbox((0, 0), my_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_xy = ((img_width - text_width) // 2, (img_height - text_height) // 2)
    text_xy = (text_xy[0] + text_xy_offset[0], text_xy[1] + text_xy_offset[1])
    
    draw.text(
        text_xy, 
        my_text, 
        font=font, 
        fill=(255, 255, 255)
    )
    
    image.save(output_image_path)
    print(f"✅ Image saved successfully to: {output_image_path}")

    absolute_image_path = os.path.abspath(output_image_path)
    
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, absolute_image_path, 3)
    print("✅ Wallpaper has been set!")

except FileNotFoundError:
    print(f"❌ Error: Cannot find '{input_image_path}'.")
except OSError:
    print(f"❌ Error: Cannot find the font '{font_path}'.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")