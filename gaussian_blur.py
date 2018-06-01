import Image
im=Image.open("1.png") #provide the name of the file your want to choose
rgb_im=im.convert("RGB")

# to provide a gaussian blur filter to the image, note you can put any filter just tweeking with the values, and  the filter can be also given to specific regions of the code, if wanted

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



from PIL import Image

data=""
for j in range(0,c-4):
	for i in range((j*a),((j+1)*a)-3):
		x=(red[i]*(-2))+ (red[i+1]*(-1))+ (red[i+a]*(-1))+(red[i+a+1]*1)+(red[i+a+2]*1)+(red[i+1+(2*a)]*1)+(red[i+2+(2*a)]*2)
		y=(green[i]*(-2))+ (green[i+1]*(-1))+ (green[i+a]*(-1))+(green[i+a+1]*1)+(green[i+a+2]*1)+(green[i+1+(2*a)]*1)+(green[i+2+(2*a)]*2)
		z=(blue[i]*(-2))+ (blue[i+1]*(-1))+ (blue[i+a]*(-1))+(blue[i+a+1]*1)+(blue[i+a+2]*1)+(blue[i+1+(2*a)]*1)+(blue[i+2+(2*a)]*2)
		data+=chr(abs(x)%256)+chr(abs(y)%256)+chr(abs(z)%256)

im=Image.fromstring("RGB",(a-3,c-4), data)
im.save("gaussian_blur.png", "PNG")

				
