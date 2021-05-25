import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

# data coordinates and values
x = [ 121.39, 126.19, 130.27, 127.42, 126.14, 125.96, 123.15, 130.5, 129.08, 122.74 ]
y = [ 13.51, 12.02, 13.11, 10.09, 15.33, 14, 10.88, 11.18, 15.78, 15.82 ]
z = [ 1.494, 1.934, 2.148, 9.155, 2.221, 8.1, 2.039, 1.916, 3.729, 7.137 ]


# target grid to interpolate to
xi = np.arange(121.0, 131.2, 0.2)
yi = np.arange(10.0, 16.035, 0.085)
xi,yi = np.meshgrid(xi,yi)

# set mask
#mask = (xi > 0.5) & (xi < 0.6) & (yi > 0.5) & (yi < 0.6)

# interpolate
zi = griddata((x,y),z,(xi,yi),method='linear')

# mask out the field
#zi[mask] = np.nan

# plot
fig = plt.figure()
ax = fig.add_subplot(111)
plt.contourf(xi,yi,zi,np.arange(0,10.01,0.01))
plt.plot(x,y,'k.')
plt.xlabel('xi',fontsize=16)
plt.ylabel('yi',fontsize=16)
plt.savefig('interpolated.png',dpi=100)
plt.close(fig)
