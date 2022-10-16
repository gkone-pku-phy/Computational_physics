from T3_export import chebyshev_expansion,chebyshev
from matplotlib import pyplot as plt 
import numpy as np 
from T4_auto_test import autoTest
from math import * 

origin = lambda x: 1/(1+25*x**2)
coeffs=chebyshev_expansion(origin,20,20)
print(coeffs)
approx = lambda x: sum([chebyshev(i)(x)*coeffs[i] for i in range(20)])
x=np.linspace(-1,1,1000)
# y1 = [approx(i) for i in x] 
# y2 = [origin(i) for i in x]
# yabs=[abs(approx(i)-origin(i)) for i in x]

data_xs = np.linspace(-1,1,41,endpoint=True)
autoTest(origin,approx,data_xs,'a','b','c')