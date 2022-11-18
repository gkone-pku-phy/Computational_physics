import numpy as np 
f = lambda x:np.exp(-x)/x
def integrate_Trapezoidal(f,a,b,points):
    x = np.linspace(a,b,points,endpoint=True)
    y= f(x)
    return (sum(y)-(y[0]+y[-1])/2)*(b-a)/(points-1) 
def integrate_simpson(f,a,b,points):
    x = np.linspace(a,b,points,endpoint=True)
    assert(points%2==1)
    n = (points-1)//2
    y=f(x)
    s = 0
    for idx,val in enumerate(y):
        if idx==0 or idx == 2*n:
            s+= val 
        elif idx % 2 == 0:
            s+= 2*val 
        else : 
            s+= 4*val 
    s*=(b-a)/6/n
    return s 
def Gauss_Chebyshev(f,a,b,points):
    x = np.arange(points)
    cosxk = np.cos(np.pi*(x+1/2)/points)
    sinxk = np.sin(np.pi*(x+1/2)/points)
    sum_ = 0
    for i in range(points):
        sum_ +=sinxk[i]*f(a+(b-a)/2*(1+cosxk[i]))
    sum_ = sum_ * (b-a)*np.pi/2/points
    # ret = cosxk*sinxk*f(a+(b-a)/2*(1+cosxk))
    # return sum(ret)*(b-a)*np.pi/(2*points)
    return sum_
from math import exp 
# f = lambda x:x
f = lambda x:np.exp(-x)/x

for points in [11,101,1001]:
    y1=integrate_simpson(f,1,100,points)
    y2=integrate_Trapezoidal(f,1,100,points)
    print(f"{points} points:Trapezoidal:{y2}\tsimpson:{y1}")
for points in [10,100]:
    y=Gauss_Chebyshev(f,1,100,points)
    print(f"points:{points},Gauss-Chebyshev:{y}")


