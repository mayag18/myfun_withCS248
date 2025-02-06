# Feb 6, 2025
# Code generated automatically by ChatGPT, based on the following prompt:
"""I have a folder with 9 images (all as .webp). I want you to write a 
Python script (with jinja2) that will generate an HTML page that 
includes a gallery of the images from my folder. This will run locally, 
it will not be uploaded on a server. 
Include a requirement.txt file to install all libraries that might be 
needed, such as jinja2 or anything else. Make sure that the images are 
all shown in the same size. 
Also, use an external CSS stylesheet, that the jinja2 template will 
make use of.
"""

import os
from jinja2 import Environment, FileSystemLoader

# Paths
IMAGE_FOLDER = "images"
TEMPLATE_FOLDER = "templates"
OUTPUT_HTML = "gallery_simple.html"

# Get all .webp images from the folder
image_files = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith(".webp")]
image_files.sort()  # Sort alphabetically for consistent order

# Setup Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER))
template = env.get_template("gallery.html")

# Render HTML with image filenames
html_output = template.render(images=image_files, image_folder=IMAGE_FOLDER)

# Write output HTML file
with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_output)

print(f"Gallery generated successfully! Open {OUTPUT_HTML} in your browser.")