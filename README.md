# mandelbrot
Learn about Mandelbrot properties and attempt to create it in the computer

After researching for 8 hours and multiple Wikipedia/Google pages later: we have success.

# PIL 
Learned about python's PIL library which is essential to convert code into image files. 

Create an image object via im = Image.new('RGB', (width, height), (0,0,0))

asigned draw function with image object via draw = ImageDraw.Draw(im)

for a certain pixel[i,j] along your canvas via draw.point(([i,j]), (color,color,color))

save the output via im.save('output.png', 'PNG')

# Sample Outputs

*First Success!*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/FIRSTSUCCESS.png?raw=true)

*Added Gray Scale*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/INVERTEDCOLOREDSUCESS.png?raw=true)

*Inverted Colors*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/COLOREDSUCCESS.png?raw=true)

*Light Blue*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/LIGHTBLUE.png?raw=true)

*Light Yellow and changed Plane*
![image](https://github.com/sedaji/mandelbrot/blob/master/pictures/reddit.png?raw=true)
