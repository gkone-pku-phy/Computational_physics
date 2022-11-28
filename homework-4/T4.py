from mpl_toolkits import mplot3d
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
ax = plt.axes(projection='3d')

xfinal = 10
xini = 0
nstep = 100000
beta = 8/3
rho = 18
sigma = 10 
xs,ys,zs = [],[],[]
x,y,z= 12,4,0
xstep = (xfinal-xini)/nstep 

xs.append(x)
ys.append(y)
zs.append(z)
cnt = 0
while cnt<nstep:
    cnt+=1
    x=x + xstep *(-beta*x+y*z)
    y=y + xstep*sigma*(z-y)
    z=z + xstep*(-y*x+rho*y-z)
    xs.append(x)
    ys.append(y)
    zs.append(z)
ax.plot3D(xs,ys,zs,'red')
# plt.show()
plt.savefig(f"T4_{beta:.2f},{rho:.2f},{sigma:.2f}.png")
    