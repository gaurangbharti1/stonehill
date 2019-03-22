import sys
from PIL import Image
im = Image.open(sys.argv[1])

im.thumbnail((100, 100), Image.ANTIALIAS)
im.save("smaller-output.png")