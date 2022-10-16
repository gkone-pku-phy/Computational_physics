# %%
from matplotlib import pyplot as plt 
import numpy as np 
from math import * 
def chebyshev(n):
    return lambda x:cos(n*acos(x))

def chebyshev_expansion(f,truncate=5,nmax=100):
    '''
    f: x\in [0,1]
    '''
    coeffs=[]
    def delta(a,b):
        return 1 if a==b else 0
    for m in range(truncate):
        c=0
        l=(2- delta(0,m))/nmax
        for n in range(nmax):
           c+= f(cos(pi*(n+0.5)/nmax))*cos(m*pi*(n+0.5)/nmax)
        c*= l 
        coeffs.append(c)
    return coeffs 


# %%
if __name__=="__main__":
    x=np.linspace(-1,1,1000)
    # y1=[[chebyshev(i)(a) for a in x] for i in range(7) ]
    # order=5 # 0-4阶
    order=7 # 0-6阶
    def origin(x):
        return log2((x+3)/2)
    expansion=chebyshev_expansion(origin,order,10)
    def f(x):
        return sum([coeff*chebyshev(i)(x) for i,coeff in enumerate(expansion)]) 

    y1 = [origin(i) for i in x]
    y2 = [f(i) for i in x]
    y3 = [f(i)-origin(i) for i in x]
    plt.plot(x,y1,label="origin")
    plt.plot(x,y2,label="expand")
    plt.xlabel("x'")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("./image/T3_order6_compare.png")
    plt.cla()
    plt.plot(x,y3)
    plt.xlabel("$x'$")
    plt.ylabel("$\hat y-y$")
    plt.savefig("./image/T3_order6_subtract.png")


    # %%



