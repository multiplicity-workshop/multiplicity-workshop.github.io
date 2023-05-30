from PIL import Image, ImageDraw
from pathlib import Path

img_dir = Path("assets/img/organizer-circles/")
filenames = ["charlie.jpg", "jamelle.jpg", "cooper.jpg", "flavio.jpg"]


for fname in filenames:
    read_path = img_dir / fname
    write_path = img_dir / (fname.split(".")[0] + "-circle.jpg")

    # open your image
    img = Image.open(read_path)

    # ensure image has an alpha channel
    img = img.convert("RGBA")

    # create a white image of the same size
    white_img = Image.new('RGBA', img.size, (255,255,255,255))

    # mask
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)

    # composite
    img = Image.composite(img, white_img, mask)

    # # draw a white solid circle
    # draw = ImageDraw.Draw(img)
    # draw.ellipse((0, 0) + img.size, outline='black', width=20)

    # save to JPEG with reduced quality for smaller file size
    img.convert("RGB").save(write_path, 'JPEG', quality=50)
