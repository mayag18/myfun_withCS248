# Feb 06, 2025
# Code generated automatically by ChatGPT, based on the following prompt:
"""The python/jinja2 code you wrote here earlier worked great. Can you add some 
CSS or JS code that when one hovers over each image, a transparent label 
covers the image to show the caption of the image. I will provide a list 
with the caption names and image file names. Also, use the caption names 
for the alt attribute."""
# This code modifies the code in the file "generate_gallery.py"

import os
from jinja2 import Environment, FileSystemLoader

# Paths
IMAGE_FOLDER = "images"
TEMPLATE_FOLDER = "templates"
OUTPUT_HTML = "gallery_captions.html"

# List of images and their captions (replace with your actual filenames & captions)
image_captions = {
    "bates.webp": "Bates Dining Hall",
    "collins.webp": "Collins Cafe",
    "el-table.webp": "El Table",
    "emporium.webp": "Emporium",
    "hoop.webp": "Cafe Hoop",
    "leaky-beaker.webp": "The Leaky Beaker",
    "lulu.webp": "Bae Pao Lu Chow Dining Room",
    "stone-d.webp": "Stone Davis Dining Hall",
    "tower.webp": "Tower Dining Hall"
}

# Filter out images that exist in the folder
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f in image_captions]

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
template = env.get_template("gallery_c.html")

# Render HTML with image filenames and captions
html_output = template.render(images=image_files, captions=image_captions, image_folder=IMAGE_FOLDER)

# Write output HTML file
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"Gallery generated successfully! Open {OUTPUT_HTML} in your browser.")
