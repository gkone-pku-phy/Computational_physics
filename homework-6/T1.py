from random import random
import numpy as np
import matplotlib.pyplot as plt 
def getval(N):
    x=np.random.rand(N)
    return np.average(np.exp(-100*(x-0.5)**2))

N=10000
samp=1000
data=np.array([getval(N) for _ in range(samp)])
string=f'N={N},var={np.var(data):.7f},avg={np.average(data):.5f}'
print(string)
plt.hist(data,density=True,bins=30)
# plt.show()
plt.savefig(f"T1_{string}.png")