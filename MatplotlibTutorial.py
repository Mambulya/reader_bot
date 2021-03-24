from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
#from IPython.display import set_matplotlib_formats, display
# import pylab  -  Numpy + MatPlotLib
"""
this script is for discovering of Matplotlib library

--------------------------Graphs creating--------------------------

# set a style
plt.style.use("seaborn-whitegrid")


# vector format
set_matplotlib_formats("svg")

# creates a x coordinates list
x = np.array([-3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3])

# creates a x**2 coordinates list
y = x**2

# draws a parabola
display(plt.plot(x, y, color='#FFC300', label="y = x^2", linewidth=3))   # 'o-c' is marker='o', linestyle='-', color='c'

# draws a hyperbola  -  negative X axis
x = np.linspace(-3, 0, 25)[:-1]
y = 1 / x
display(plt.plot(x, y, 'r', color ='#DAF7A6', label="y = 1/x, x != 0", linewidth=4))

# draws a hyperbola  -  positive X axis
x = np.linspace(0, 3, 25)[1:]
y = 1 / x
display(plt.plot(x, y, color ='#DAF7A6', linewidth=4))

# the axis editing
plt.ylabel(" the Y axis of points")
plt.xlabel(" the X axis of points")
plt.title("Y-functions")
plt.legend()
plt.grid(True)

plt.show()

--------------------------Graphs creating on image--------------------------

im = np.array(Image.open("SAMPLES/glaces.jpg"))
x = [190, 190, 570, 570]
y = [200, 500, 500, 200]

# default settings
plt.axis("off")

plt.imshow(im)

plt.plot(x, y, 'o-', color='#CCCCFF')

# first and last points match
plt.plot([x[0], x[-1]], [y[0], y[-1]], '#CCCCFF')

# plotting editing
plt.title("Plotting: 'book.jpg'")
plt.show()

--------------------------Image counter--------------------------

im = np.array(Image.open("SAMPLES/glaces.jpg"))

plt.imshow(im)
print("5")
plt.ginput(5)
print("END")

plt.show()
"""
