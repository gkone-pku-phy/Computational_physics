from copy import deepcopy 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from math import *

tstep = 0.001
nx= 100
xmin = 0
xmax = 2
frames= 3000
xstep = (xmax-xmin)/nx

x = np.zeros(nx)
x_prev = np.zeros(nx)
x_ = range(nx)
delta = 0.042
print(tstep/xstep*(1+4*(delta**2/xstep**2)))
def init(x):
    for i in range(len(x)):
        x[i]= cos(pi*i*xstep)
        x_prev[i]=cos(pi*i*xstep)



def KdV_FillMatrix(mat,x):
    len_=len(mat)
    alpha = tstep/xstep/2
    beta = delta**2/xstep**2
    for i in range(len_):
        
        mat[i][(i-2) % len_]=-beta *alpha
        mat[i][(i-1)%len_] = 2*beta*alpha-alpha*x[i]
        # mat[i][(i-1)%len_] = 2*beta*alpha-2*alpha*(x[i]+x[(i-1)%len_])
        mat[i][i] = 1
        mat[i][(i+1)%len_] = -mat[i][(i-1)%len_]
        # mat[i][(i+1)%len_] = -2*beta*alpha +2* alpha*(x[(i+1)%len_]+x[i])
        mat[i][(i+2)%len_] = -mat[i][(i-2) % len_]
    
def evolve(dt):
    global x    
    # mat=np.zeros((nx,nx))
    # KdV_FillMatrix(mat,x)
    # x = np.linalg.solve(mat,x)
    # print(x)
    x_cpy = deepcopy(x)
    for i in range(nx):
        # x[i] = x_cpy[i]-dt/xstep/2*((x_cpy[(i+1)%nx]+x_cpy[i]+x_cpy[(i-1)%nx])/3*(x_cpy[(i+1)%nx]-x_cpy[(i-1)%nx])- \
        #         delta**2/xstep**2*(x_cpy[(i+2)%nx]-2*x_cpy[(i+1)%nx]+2*x_cpy[(i-1)%nx]-x_cpy[(i-2)%nx]))

        # x[i] = x_cpy[i]-tstep/xstep/6*(x_cpy[(i-1)%nx]+x_cpy[i]+x_cpy[(i+1)%nx])*(x_cpy[(i+1)%nx]-x_cpy[(i-1)%nx])-\
        #    tstep/2/xstep**3*delta**2* (x_cpy[(i+2)%nx]-2*x_cpy[(i+1)%nx]+2*x_cpy[(i-1)%nx]-x_cpy[(i-2)%nx])
        
        x[i] = x_prev[i]-2*tstep/xstep/6*(x_cpy[(i-1)%nx]+x_cpy[i]+x_cpy[(i+1)%nx])*(x_cpy[(i+1)%nx]-x_cpy[(i-1)%nx])-\
           2*tstep/2/xstep**3*delta**2* (x_cpy[(i+2)%nx]-2*x_cpy[(i+1)%nx]+2*x_cpy[(i-1)%nx]-x_cpy[(i-2)%nx])
        x_prev[i]=x_cpy[i]

        
init(x)
fig,ax = plt.subplots()
ax.set_ylim(-1,3)
line, = ax.plot(x_,x)
txt=ax.text(0,0,"time=0s")
t=0.0
def update(num):
    global t
    t+=tstep
    evolve(tstep)
    line.set_ydata(x)
    txt.set_text(f"time={t:.3f}s")
    return line,
ani = FuncAnimation(fig, update,interval=20,frames=frames)
plt.show()
# ani.save(f"T1_delta={delta:.3f},dt={tstep:.3f},nx={nx}.mp4")
