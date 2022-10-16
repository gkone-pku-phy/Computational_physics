from enum import auto
from matplotlib import pyplot as plt 
import numpy as np 
from math import * 
import functools
from operator import mul ,add
from T4_auto_test import autoTest

def lagrange(i,xs):
    '''
    return a function L_i(x) such that:
    L_i(x_i)=1
    L_i(x_j)=0 ,i\ne g
    i,j = 0,1,...,n-1
    '''
    return lambda x:functools.reduce(
        mul,[(x-xs[j])/(xs[i]-xs[j]) 
        for j in filter(
            lambda j:j!=i ,range(len(xs))
        )]
        )
def lagrange_approximation(f,xs):
    return lambda x:functools.reduce(add,[
        f(xs[i])*lagrange(i,xs)(x) for i in range(len(xs))
    ])
xs=np.linspace(-1,1,21,endpoint=True)

origin = lambda x: 1/(1+25*x**2)
approx_f = lagrange_approximation(origin,xs)
autoTest(origin,approx_f,xs,'b','c')
