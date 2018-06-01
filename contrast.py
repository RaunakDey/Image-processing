# to change the contrast of the image, note you can put any filter just tweeking with the values, and  the filter can be also given to specific regions of the code, if wanted
import Image
im=Image.open("1.png")   #provide the name of the file your want to choose
rgb_im=im.convert("RGB")

(a,c)=im.size


red=[]
green=[]
blue=[]

#change of contrast is done by changing the RGB values equally in any direction until une of them reaches th boundary 0 or 255. then that value is held constant and other values are changes to further change the constrast

t=input("addition of contrast")
for j in range (0,c):
	for i in range (0,a):
		r,g,b=rgb_im.getpixel((i,j))
		if (r+t)<=255:
			red.append(r+t)
		else: 
			red.append(255)
		if (g+t)<=255:
			green.append(g+t)
		else: 
			green.append(255)
		if (b+t)<=255:
			blue.append(b+t)
		else: 
			blue.append(255)					
	


from PIL import Image

data=""
for j in range(0,c-4):
	for i in range((j*a),((j+1)*a)-3):
		x=red[i+a+1]
		y=green[i+a+1]
		z=blue[i+a+1] #blue[i]*(0))+ (blue[i+1]*(0))+ (blue[i+a]*(0))+(blue[i+a+1]*(-1))+(blue[i+a+2]*1)+(blue[i+1+(2*a)]*0)+(blue[i+2+(2*a)]*0)
		data+=chr(abs(x))+chr(abs(y))+chr(abs(z))

im=Image.fromstring("RGB",(a-3,c-4), data)
im.save("edge_enhanced_pic2.png", "PNG")

				
