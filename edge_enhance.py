import Image
im=Image.open("frame2666.jpg") #provide the name of the file your want to choose
rgb_im=im.convert("RGB")

(a,c)=im.size


red=[]
green=[]
blue=[]


for j in range (0,c):
	for i in range (0,a):
		r,g,b=rgb_im.getpixel((i,j))
		red.append(r)
		green.append(g)
		blue.append(b)


#edge enhancement is just a matric multiplication to the square patches chosen from the image, note the matrix is non-invertible so that once the filter is applied it can't be returned to the orginal picture.

from PIL import Image

data=""
for j in range(0,c-4):
	for i in range((j*a),((j+1)*a)-3):
		x=(red[i]*(0))+ (red[i+1]*(0))+ (red[i+a]*(0))+(red[i+a+1]*(-1))+(red[i+a+2]*1)+(red[i+1+(2*a)]*0)+(red[i+2+(2*a)]*0)
		y=(green[i]*(0))+ (green[i+1]*(0))+ (green[i+a]*(0))+(green[i+a+1]*(-1))+(green[i+a+2]*1)+(green[i+1+(2*a)]*0)+(green[i+2+(2*a)]*0)
		z=(blue[i]*(0))+ (blue[i+1]*(0))+ (blue[i+a]*(0))+(blue[i+a+1]*(-1))+(blue[i+a+2]*1)+(blue[i+1+(2*a)]*0)+(blue[i+2+(2*a)]*0)
		data+=chr(abs(x))+chr(abs(y))+chr(abs(z))

im=Image.fromstring("RGB",(a-3,c-4), data)
im.save("edge_enhanced_LML.png", "PNG")

				
