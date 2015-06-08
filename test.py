from PIL import Image, ImageDraw
import PIL.ImageOps  

base = Image.open("img.jpg")
mask = Image.new('RGBA', base.size, (255,255,255,0))
x, y = base.size
var = y/20 

# Define triangle mask position
(originx,originy) = (x/3,2*y/3)
trih = 12*var  #fix formular for triangle height
triw = 4.2*var #fix formular for triangle width
polygonpos = [(originx,originy),
(originx+triw,originy), 
(originx+triw/2,originy-trih)]

# Create mask
draw = ImageDraw.Draw(mask,'RGBA')
draw.polygon(polygonpos,(0,0,0,255))

del draw
mask.save("mask.png")

# Get the Alpha band from the template
tmplt = Image.open('mask.png')
A = tmplt.split()[3]
print(A)

#make one piece of triangle
[R,G,B]=base.split()
apiece = Image.merge('RGBA', (R, G, B, A))
box =(originx,(originy-trih),(originx+trih),originy)
crop=apiece.crop(box)
crop.save('apiece.png')

#make new canvas
canvas=Image.new('RGBA',(trih,trih), (255,255,255,0))

apiece = apiece.transpose(Image.ROTATE_180)
canvas.paste(apiece.png,box)
canvas.save("canvas.png")

#mkkcldwkc;wec



# write to stdout
base.save("testpic.png")
