from scipy import integrate
from math import *
from T4 import sum_in_sphere
def sum_fourier(r_sqr):
    q=sqrt(0.5)
    def func(t,q,k):
        return exp(t*q**2)*(pi/t)**1.5*exp(-pi**2*k**2/t)
    err=0
    if r_sqr == 0:
        ret1 = 0
    else:
        ret1 = integrate.quad(func,0,1,(q**2,sqrt(r_sqr)),err)[0]
    if(err!=0):
        print(f"error:{err}")
    def func2(r_sqr):
        return exp(-r_sqr+q**2)/(r_sqr-q**2)
    return ret1 + func2(r_sqr)
def func3(t):
    return 2/sqrt(pi)*exp(t**2)
q=sqrt(0.5)
rets = []
for i in range(1,10):
    s1 = sum_in_sphere(sum_fourier,0,i)
    ret = s1-2*pi**1.5 * exp(q**2 )+2*pi**2 *q * integrate.quad(func3,0,q)[0]
    rets.append(ret)
    print(i,ret)
