# mandelbrot
Learn about Mandelbrot properties and attempt to create it in the computer

8 hours of researching multiple Wikipedia/Google pages,

2 Hours of planning with pseudocode, and

1 Hour of debugging later: We have Success!


# Sample Outputs

<span style="text-align:center;display:block">*First Success!*</span>
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/FIRSTSUCCESS.png?raw=true)

*Added Gray Scale*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/INVERTEDCOLOREDSUCESS.png?raw=true)

*Inverted Colors*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/COLOREDSUCCESS.png?raw=true)

*Light Blue*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/LIGHTBLUE.png?raw=true)

*Light Yellow and changed Plane*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/reddit.png?raw=true)


# PIL 
Learned about python's PIL library which is essential to convert code into image files. 

Create an image object via im = Image.new('RGB', (width, height), (0,0,0))

asigned draw function with image object via draw = ImageDraw.Draw(im)

for a certain pixel[i,j] along your canvas via draw.point(([i,j]), (color,color,color))

save the output via im.save('output.png', 'PNG')
