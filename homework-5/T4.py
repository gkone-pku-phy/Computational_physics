from random import random 
import numpy as np
from scipy.special import gamma

N=100
k=10
range_=list(np.linspace(0,1,11))
cnt=[[0 for __ in range(10000)] for _ in range(k)]
c2=[]
for exp in range(10000):
    for i in range(N):
        tmp = random()
        for idx in range(k):
            if(range_[idx]<tmp<range_[idx+1]):
                cnt[idx][exp]+=1
    chi2_ = 0
    for i in range(k):
        chi2_ += ( cnt[i][exp]-N/k)**2/(N/k)
    c2.append(chi2_)
import matplotlib.pyplot as plt 
def chi2(x,n):
    return 1/(2**(n/2)*gamma(n/2))*(x**(n/2-1)*np.exp(-x/2))
xmax=30
x = np.linspace(0,xmax)
y = chi2(x,k-1)

print(c2)
plt.hist(c2,xmax,range=(0,xmax),density=True)
plt.plot(x,y)
plt.show()
# ax.hist()
