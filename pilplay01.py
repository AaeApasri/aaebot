import PIL
from PIL import Image, ImageFilter, ImageDraw




#load image
pic = Image.open("img.jpg")
polygon = ImageDraw.Draw(im)

#get size 
x, y = pic.size
var = y/20  # number has to be more than 18

# create mask
polygonpos = [(x/3,2*y/3), #origin
(x/3+4.2*var,2*y/3), 
(x/3+2.1*var,y*2/3-12*var)]

# draw polygon
PIL.ImageDraw.Draw.polygon(polygonpos, fill=0, outline=None)


"""maskIm = Image.new('L', (imArray.shape[0], imArray.shape[1]), 0)
ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
#mask = numpy.array(maskIm)

#do sth with image
#pic= pic.filter(ImageFilter.EDGE_ENHANCE_MORE)
im1 = pic.quantize(colors=32, method=None, kmeans=0, palette=None)
#im2 = pic.filter(ImageFilter.FIND_EDGES)
 
print(type(Image))

im1.save("newimage.png")"""