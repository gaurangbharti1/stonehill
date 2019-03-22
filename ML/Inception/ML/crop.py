import sys,os
from PIL import Image
im = Image.open(sys.argv[1])

im.thumbnail((100, 100), Image.ANTIALIAS)
im.save("smaller-output.jpg")
os.system("python3 ./label_image.py smaller-output.jpg")