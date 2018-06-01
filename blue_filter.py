# to provide a blue filter to the image, note you can put any filter just tweeking with the values, and  the filter can be also given to specific regions of the code, if wanted
import Image

im=Image.open("1.png")   #provide the name of the file your want to choose
rgb_im=im.convert("RGB")

(a,c)=im.size


red=[]
green=[]
blue=[]


for j in range (0,c):
	for i in range (0,a):
		r,g,b=rgb_im.getpixel((i,j))
		red.append(0)
		green.append(0)
		blue.append(b)



from PIL import Image

data=""
for j in range(0,a*c):
		x=0
		y=0
		z=blue[j]
		data+=chr(x)+chr(y)+chr(z)

im=Image.fromstring("RGB",(a,c), data)
im.save("blue filter.png", "PNG")

				
