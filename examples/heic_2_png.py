import glob
from vidlib.images_tools import heic_2_png

lst = glob.glob("/Users/andrey.matveev/Downloads/*.heic")

for l in lst:
    heic_2_png(l)
