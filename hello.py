import PIL
from PIL import Image

#load image
pic = Image.open("img.jpg")
print (pic.size)
pixels = pic.load()

xsize, ysize = pic.size

#iterate every pixels and invert rgb value
for x in range (xsize):
	#print(x)
	for y in range(ysize):
		#print ((x,y))
		r,g,b = pixels[x,y]
		r= 255-r
		g= 255-g
		b= 255-b
		pixels[x,y]=r,g,b
pic.save("newimage.jpg")