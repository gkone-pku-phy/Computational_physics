from math import cos
from matplotlib import pyplot as plt 
import numpy as np 
x= np.linspace(0,0.9,1000)
b_2_=-1.19082
c_1_=0.13132
c_2_=-0.58316
b_1_=0.00000
d_1_=1.00000
d_2_=0.93590
a_1_=-0.66156
a_2_=1.32313

a_1=-0.62916
a_2=-1.12487
b_1=0.19943
b_2=-0.93305
c_1=0.00000
c_2=-0.44017
d_1=1.00000
d_2=0.93590
x_1=0.6

f=lambda x:a_1_*x**3+b_1_*x**2+c_1_*x+d_1_ if x<0.6 else \
    a_2_*(x-x_1)**3+b_2_*(x-x_1)**2+c_2_*(x-x_1)+d_2_ 
g=lambda x:cos(x**2)
h=lambda x:a_1*x**3+b_1*x**2+c_1*x+d_1 if x<0.6 else \
    a_2*(x-x_1)**3+b_2*(x-x_1)**2+c_2*(x-x_1)+d_2 
y1=[f(_) for _ in x]
y2=[g(_) for _ in x]
y3=[h(_) for _ in x]
plt.plot(x,y1,label="a curve")
plt.plot(x,y2,label="origin curve")
plt.plot(x,y3,label="b curve")
plt.legend()
plt.show()