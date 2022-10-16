from T4_auto_test import autoTest
import numpy as np 
from math import *
from Spline_Interpolation import cubic_spline_interpolation
if __name__=="__main__":

    data_xs = np.linspace(-1,1,21,endpoint=True)
    origin = lambda x: 1/(1+25*x**2)
    a,b,c,d,f=cubic_spline_interpolation(origin,data_xs)
    
    points=np.linspace(-1,1,41)
    autoTest(origin,f,points,'b')
