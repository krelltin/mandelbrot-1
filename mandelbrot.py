#! /usr/bin/python3
from PIL import Image, ImageDraw

z = [None] * 80
def mandelbrot(c):
	for n in range(80):
		if n > 0:
			z[n] = z[n-1]**2 + c
			if abs(z[n]) > 2:
				return n
		elif n == 0:
			z[n] = n
	return n

# Image size (pixels)
width = 3840
height = 2160 

realNeg = -2
realPos = 1
imagiNeg = -1
imagiPos = 1

realIncrement = (realPos - realNeg) / width
imagiIncrement = (imagiPos - imagiNeg) / height

realPlots = [None] * width
imagiPlots = [None] * height

for i in range(width):
	realNeg += realIncrement
	realPlots[i] = realNeg
for i in range(height):
	imagiNeg += imagiIncrement
	imagiPlots[i] = imagiNeg

im = Image.new('RGB', (width, height), (0, 0, 0))
draw = ImageDraw.Draw(im)

# color = 0
for i in range(width):
	for j in range(height):
		c = complex(realPlots[i],imagiPlots[j])
		output = mandelbrot(c)
		color = (255 - int(output * 3.1875))
		draw.point(([i,j]), (color, color, color))

im.save('output.png', 'PNG')