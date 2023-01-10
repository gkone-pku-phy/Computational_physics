from random import random
import numpy as np
import matplotlib.pyplot as plt 

def getval(): #get a f(x) where x is random
    x=np.random.rand(9)
    return np.exp(-100*sum((x-0.5)**2))
N=10000000 #N sample points to calculate an integral
data = np.array([getval() for _ in range(N)])
print(np.average(data))