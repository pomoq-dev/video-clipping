import math
import os.path

from src.vidliboba import files_tools
from PIL import Image

DIRECTORY = '..'
RES_DIRECTORY = '../images_new_girl_new'
files_tools.clear_directory(RES_DIRECTORY)

images = files_tools.list_full_paths(DIRECTORY, only_format='.png')
for image_path in images:
    img = Image.open(image_path)
    indent = 1/68 * img.width
    box = (math.floor(indent), math.floor(indent), math.floor(img.width - indent), math.floor(img.height - indent))
    img2 = img.crop(box)

    basename = os.path.basename(image_path)
    res_path = os.path.join(RES_DIRECTORY, basename)
    img2.save(res_path)

