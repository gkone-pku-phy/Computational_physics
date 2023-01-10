from matplotlib import pyplot as plt
from math import *
import numpy as np
from random import randint ,random
from tqdm import trange
import json 
data=json.load(open("1.json",'r'))
Temp = list(map(lambda x:x['Temperature'],data))
datas = list(map(lambda x:x['data'],data))

E,Susc,EVar,SuscVar=[list(map(lambda t:t[i],datas)) for i in range(4)]
# print(E,Susc,EVar,SuscVar,file=open("1.txt",'w'))
fig,axes= plt.subplots(nrows=2,ncols=2)
axes[0][0].scatter(Temp,E,s=5)
axes[0][1].scatter(Temp,Susc,s=5)
axes[1][0].scatter(Temp,EVar,s=5)
axes[1][1].scatter(Temp,SuscVar,s=5)
axes[0][0].set_title("Temperature-Energy")
axes[0][1].set_title("Temperature-Magnetization")
axes[1][0].set_title("Temperature-Capacity")
axes[1][1].set_title("Temperature-Susceptibility")
plt.show()