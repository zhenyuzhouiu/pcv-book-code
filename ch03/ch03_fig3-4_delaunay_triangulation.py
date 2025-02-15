import numpy as np  # -*- coding: utf-8 -*-
# import matplotlib.delaunay as md
from scipy.spatial import Delaunay
from pylab import *
from numpy import *

x, y = array(random.standard_normal((2, 100)))
# centers,edges,tri,neighbors = md.delaunay(x,y)
tri = Delaunay(np.c_[x, y]).simplices
figure()
gray()
subplot(121)
axis('off')
plot(x, y, '*')
for t in tri:
    t_ext = [t[0], t[1], t[2], t[0]]  # add first point to end
    subplot(122)
    plot(x[t_ext], y[t_ext], 'r')
plot(x, y, '*')
axis('off')
show()
