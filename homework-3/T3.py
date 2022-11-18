import scipy 
import numpy as np 
import sympy
dx = 1e-7
def diff(f,x):
    return (f(x+dx)-f(x))/dx
def binary_division(f,a,b,prec):
    assert(a<b and f(a)*f(b)<0)
    min_,max_ = a,b
    div = (max_+min_)/2
    
    while(max_-min_>prec):
        print(div)
        r1 = f(div)*f(min_)
        if r1<0:
            max_=div
        elif r1 ==0:
            return div 
        else:
            min_=div 
        div = (max_+min_)/2
    return div 
def Newton_ralphson(f,start,prec):
    '''
    start is the starting point of iteration.
    '''
    x_prev = 0
    x= start 
    while(abs(f(x))>prec or abs(x-x_prev)>prec):
        x,x_prev = x-f(x)/diff(f,x),x
    return x

def secant(f,start,prec):
    fpstart = diff(f,start)
    x_prev = -100
    flag_start = True
    x = start 
    cnt = 0
    while abs(f(x))>prec or (x-x_prev)>prec: 
        cnt += 1
        # print(f"x:{x},prev:{x_prev},x-x_prev:{x-x_prev},f(x):{f(x)}")
        if flag_start:
            flag_start = False 
            x,x_prev = x-f(x)/fpstart,x 
        else:
            x,x_prev = x-f(x)/((f(x)-f(x_prev))/(x-x_prev)),x
        # if cnt >= 100:
        #     break
    return x
from math import sin 
f = lambda x:x**2-4*x*sin(x)+4*sin(x)**2
x=binary_division(f,-10,10,1e-6)
# x = Newton_ralphson(f,3,1e-7)
print(x)
# x = secant(f,3,1e-7)
# print(x)