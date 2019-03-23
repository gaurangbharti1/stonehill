import sys,os
from PIL import Image
im = Image.open(sys.argv[1])

im.thumbnail((100, 100), Image.ANTIALIAS)
im.save("smaller-output.jpg")
os.system("Python3 ML/Inception/ML/label_image.py smaller-output.jpg")