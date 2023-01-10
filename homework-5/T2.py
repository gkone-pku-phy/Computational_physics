from math import *
from copy import deepcopy 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
n0=8
m0=8
xlim = [0,1]
ylim = [0,1]
tlim = [0,0.05]
frames = 80
tstep = (tlim[1]-tlim[0])/frames
xmid = (xlim[1]-xlim[0])/2
ymid = (ylim[1]-ylim[0])/2
def T0(x,y):
    return exp((-(x-xmid)**2-(y-ymid)**2)/0.13)
U = np.zeros((2,n0,m0),dtype=np.double) #fourier变换后的矩阵
def evolve(dt):
    # print(max(U[1].reshape(-1)), np.unravel_index(np.argmax(U[1], axis=None), U[1].shape))
    for n in range(n0):
        for m in range(m0):
            # tmp = U[1][n][m]
            U[1][n][m] = U[1][n][m] +dt*D*(-n**2-m**2)*pi**2 *U[1][n][m]
            # U[0][n][m]=tmp
    getMat(T)

def getMat(T):# inverse transform
    for x in range(p):
        for y in range(q):
            T[x][y]=0
            for n in range(n0):
                for m in range(m0):
                    T[x][y] += U[1][n][m] * sin(n*pi*x/p)*cos(m*pi*y/q)
p=q=70
D=1
T = np.zeros((p,q),dtype=np.double) # 实际坐标矩阵

for n in range(n0):
    for m in range(m0):
        flag=1 if m==0 else 0
        for k in range(p):
            xk=2*k/p
            for l in range(q):
                yl = 2*l/q
                U[0][n][m]+= T0(xk,yl)*sin(n*pi*xk)*cos(m*pi*yl)*(4/(p*q))*1/(1+flag)
                U[1][n][m]+= T0(xk,yl)*sin(n*pi*xk)*cos(m*pi*yl)*(4/(p*q))*1/(1+flag)
getMat(T)
fig, ax = plt.subplots()
num_frames = frames
row, col = p,q

img = ax.imshow(np.zeros((row, col)), cmap=plt.cm.cool,extent=[*(xlim+ylim)],vmin=0, vmax=max(T.reshape(-1)), origin='lower')
fig.colorbar(img) #add colorbar

text = ax.text(0,0,'time=0s')
def update(i):
    evolve(tstep)
    img.set_data(T)
    vmin,vmax = max(T.reshape(-1)),min(T.reshape(-1))
    print(f'{i}/{frames}')
    img.set_clim(vmin,vmax)
    text.set_text(f'time={i*tstep:.4f}s')
ani = FuncAnimation(fig, update, frames=num_frames,interval=50,)
ani.save("T2_.mp4")
# plt.show()
