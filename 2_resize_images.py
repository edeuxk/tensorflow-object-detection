# Author Eddy Almeida
# github : https://github.com/edeuxk/tensorflow-object-detection
import PIL
from PIL import Image
import glob, os

mywidth = 600

for infile in glob.glob("images/*.png"):
	img = Image.open(infile)
	file, ext = os.path.splitext(infile)
	wpercent = (mywidth/float(img.size[0]))
	print('resizing : ' + file)
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((mywidth, hsize), PIL.Image.ANTIALIAS)
	img.save("data/" + file + ".resized.jpg", "JPEG")