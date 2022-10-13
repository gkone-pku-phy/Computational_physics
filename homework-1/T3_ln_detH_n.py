from math import *
import numpy as np 
from matplotlib import pyplot as plt
from x2fig import get_linear_graph
def logc(n):
    return sum([log(factorial(i)) for i in range(1,n)])
def logH(n):
    return 4*logc(n)-logc(2*n)
# y=[]
# for i in range(1,20):
#     y.append(logH(i))
i=np.arange(1,20)
i_sqr = [x**2 for x in i]
y=[logH(x) for x in i]
f= lambda x:-2*log(2)*x**2 
yp=[f(x) for x in i]
# plt.plot(i,y)
# plt.xlabel("n")
# plt.ylabel("$\ln\det H_n$")
# plt.savefig("homework-1/ln_det_H_n.png")

get_linear_graph(i_sqr,y,"$n**2$","$\\ln\\det H_n$",filename="homework-1/intp.png")