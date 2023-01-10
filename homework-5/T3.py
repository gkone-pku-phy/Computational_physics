import matplotlib.pyplot as plt 
import numpy as np 
import math 
from matplotlib.animation import FuncAnimation
import sys 
if(len(sys.argv)!=2): #require a number
    sys.exit(0)
xlim=[0,1]
ylim=[0,1]
tlim=[0,int(sys.argv[1])]
Nx=30
Ny=80
Nt=400 
xstep = (xlim[1]-xlim[0])/Nx
ystep = (ylim[1]-ylim[0])/Ny
tstep = (tlim[1]-tlim[0])/Nt
l = 1

u = np.zeros((Nt,Nx+2,Ny+2),dtype=np.double) #留出边界值0
x=1/Nx*np.arange(Nx).reshape((-1,1))
y= 1/Ny*np.arange(Ny)
u[0][1:-1,1:-1]=np.sin(np.pi*x)*np.sin(2*np.pi*y)
for t in range(1,Nt):
    if t==1:
        u[t][1:-1,1:-1] = u[t-1][1:-1,1:-1]+ tstep**2*l * (\
            (u[t-1][:-2,1:-1]-2*u[t-1][1:-1,1:-1]+u[t-1][2:,1:-1])/xstep**2+\
            (u[t-1][1:-1,:-2]-2*u[t-1][1:-1,1:-1]+u[t-1][1:-1,2:])/ystep**2 \
            )
    else:
        u[t][1:-1,1:-1] =-u[t-2][1:-1,1:-1]+2*u[t-1][1:-1,1:-1]+ tstep**2*l * (\
            (u[t-1][:-2,1:-1]-2*u[t-1][1:-1,1:-1]+u[t-1][2:,1:-1])/xstep**2+\
            (u[t-1][1:-1,:-2]-2*u[t-1][1:-1,1:-1]+u[t-1][1:-1,2:])/ystep**2 \
            )
    
fig, ax = plt.subplots(1,1)
img = ax.imshow(u[0],cmap = plt.cm.hot,extent = [*(xlim+ylim)])
fig.colorbar(img)
text = ax.text(0,0,'time=0s')
def update(i):
    img.set_data(u[i])
    print(i)
    text.set_text(f'time={i*tstep:.4f}s')
ani = FuncAnimation(fig,update,frames = Nt,interval=50)
dt0=1/math.sqrt(l)*(Nx**2+Ny**2)**(-1/2)
print(tstep,dt0)

filename = f"T3_Dt={tstep:.4f},Dx={xstep:.3f},Dy={ystep:.3f}"
if(tstep<=dt0):
    filename+=',stable'
else:
    filename+=',unstable'
ani.save(filename+'.mp4')
plt.show()