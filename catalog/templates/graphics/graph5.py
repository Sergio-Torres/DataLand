import importlib
importlib.import_module('mpl_toolkits').__path__
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np 

from bokeh.plotting import figure, output_file, show

p = plt.figure()

axis = Axes3D(p)

def function(x,y):
    return ((x**2)-(y**2))
#varuables
miniLimX = -3
maxLimX= 3
minLinY = -3
maxLimY = 3

x = np.linspace(minLimX, maxLimX,40)
y = np.linspace(minLimY, maxLimY,40)

x,y = np.meshgrid(x,y)
#define z
z = function(x, y) 

axis.plot_wireframe(x,y,z, cmap='Spectral') 

axis.set_xlabel('X axis')
axis.set_ylabel('Y axis')
axis.set_zlabel('Z axis')

output_file("graph5.html")

show(p)