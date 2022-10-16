# %%
from T4_auto_test import *
from Spline_Interpolation import cubic_spline_interpolation
import numpy as np 
from math import *
t=list(range(9))

x=lambda t:cos(t*pi/4)*(1-cos(t*pi/4))
y=lambda t:sin(t*pi/4)*(1-cos(t*pi/4))
ax,bx,cx,dx,fx=cubic_spline_interpolation(x,t)
ay,by,cy,dy,fy=cubic_spline_interpolation(y,t)
print(ax,bx,cx,dx)
print(ay,by,cy,dy)


# %%

ax1=plt.subplot(111,projection="polar")
sample_phi=np.linspace(0,2*pi,1000)
r = [1-cos(phi) for phi in sample_phi]
t_=np.linspace(0,8,1000)
rho=[sqrt(fx(ti)**2+fy(ti)**2) for ti in t_]
phi=[atan2(fy(ti),fx(ti)) for ti in t_]
# plt.plot(t_,[fx(i) for i in t_])
# plt.show()
ax1.plot(sample_phi,r,label="original")
ax1.plot(phi,rho,label="approximation")
rho,phi =[1-cos(pi*t/4)  for t in range(9)],[pi*t/4 for t in range(9)]
for r,p in zip(rho,phi):
    ax1.scatter([p],[r],c="r")
plt.legend()
plt.show()

# %%



