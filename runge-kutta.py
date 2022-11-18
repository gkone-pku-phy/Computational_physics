from matplotlib import pyplot as plt
from math import *
import numpy as np
import scipy
import sympy

def runge_kutta_2(f,init,start,step,count):
    '''
    u' = f(u,t)
    u(start)= init 
    u(start+step*(count-1)) = ?
    return 'count' numbers of u
    函数值平均
    '''
    t=start
    u=init
    result = []
    for i in range(count):
        result.append(u)
        k1=f(t,u)
        k2=f(t+step,u+step*k1)
        u+= step/2*(k1+k2)
        t+= step
    return result 
def runge_kutta_2_(f,init,start,step,count):
    '''
    中点平均
    '''
    t=start
    u=init
    result = []
    for i in range(count):
        result.append(u)
        k1=f(t,u)
        k2=f(t+step/2,u+step/2*k1)
        u+= step*k2
        t+= step 
    return result 
def runge_kutta_4(f,init,start,step,count):
    t=start 
    u = init 
    result = [] 
    for i in range(result):
        pass
def euler(f,init,start,step,count):
    t=start
    u=init 
    result = []
    for i in range(count):
        result.append(u)
        u+= step * f(t,u)
        t+= step
    return result 

def f(t,y):
    return -y
class Vector:
    def __init__(self,*args):
        self.vec=args 
        self.len = len(args)
    def __add__(self,v):
        return Vector(*[v1+v2 for v1,v2 in zip(self,v)])
    def __sub__(self,v):
        return Vector(*[v1-v2 for v1,v2 in zip(self,v)])
    def __mul__(self,c):
        return Vector(*[c*v for v in self])
    def __rmul__(self,c):
        return self*c
    def __truediv__(self,c):
        return Vector(*[v/c for v in self])
    def __repr__(self):
        return f"Vector({','.join(map(str,self))})"
    def __iter__(self):
        for ele in self.vec:
            yield ele
    
if __name__=="__main__":
    count=10000
    stop = 100
    start = 0
    k=100
    step = (stop-start)/count
    y1=runge_kutta_2(f,1,start,step*k,count//k)
    # y2=runge_kutta_2_(f,1,start,step*2,count//2)
    x_ = np.linspace(start,stop,count//k)
    y3=euler(f,1,0,step,count)
    x=np.linspace(0,stop,count)
    plt.plot(x_,np.log(y1),'r',label="1")
    # plt.plot(x_,np.log(y2),'b',label="2")
    plt.plot(x,np.log(y3),'g',label="3")
    plt.plot(x,-x,'y',label='real')
    plt.legend()
    plt.show()