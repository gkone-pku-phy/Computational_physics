import numpy as np 
from math import *
from matplotlib import pyplot as plt 
def autoTest(origin,approx,xs,*args):
    if 'a' in args:
        print("x\toriginal func\tapproximation\tabs")
        print("------------------------------------------")
        for x in xs:
            print(f"{x:.4f}\t{origin(x):+.4f}\t{approx(x):+.4f}\t{abs(approx(x)-origin(x)):+.4f}")
    
    plot_xs=np.linspace(min(xs),max(xs),10000)
    original_y=[origin(t) for t in plot_xs]
    approx_y = [approx(t) for t in plot_xs]
    if 'b' in args:
        plt.plot(plot_xs,original_y,label="original")
        plt.plot(plot_xs,approx_y,label="approximation")
        plt.legend()
        plt.show()
        plt.cla()
    if 'c' in args:
        abs_=[abs(y1-y2) for y1,y2 in zip(original_y,approx_y)]
        plt.plot(plot_xs,abs_)
        plt.show()
        plt.cla()
