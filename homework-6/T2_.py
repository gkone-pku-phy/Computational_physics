from matplotlib import pyplot as plt
from math import *
import numpy as np
from random import *
from tqdm import trange
import json,os ,sys
from signal import signal,SIGINT
import multiprocessing,threading

def sigint_handler(signum, frame):
    print('SIGINT received. Program shutting down. Saving data.')
    save_data()
    sys.exit(0)
def save_data():
    global datas
    if not os.path.exists("1.json"):
        origin_data=[]
    else:
        with open("1.json",'r') as f:
            origin_data = json.load(f)
    Temp = list(map(lambda x:x[0], datas))
    data_ = list(map(lambda x:x[1:], datas))
    origin_data+=[{"Temperature":T ,"data":d} for T,d in zip(Temp,data_)]
    with open("1.json","w") as f:
        json.dump(origin_data,f)
    return
signal(SIGINT,sigint_handler)

d = [(0,-1),(0,1),(1,0),(-1,0)]
def getEnergy(state):
    # k1=size-np.count_nonzero(state[2:,:]^state[1:-1,:])
    # k2=size-np.count_nonzero(state[:-2,:]^state[1:-1,:])
    # k3=size-np.count_nonzero(state[:,2:]^state[:,1:-1])
    # k4 = size-np.count_nonzero(state[:,:-2]^state[:,1:-1])
    # return k1+k2+k3+k4 
    E=0
    for i in range(nx):
        for j in range(ny):
            for x,y in nearby(i,j):
                if(state[x,y]==state[i,j]):
                    E+=1
    return -E/2
def nearby(x,y):
    return [((x+dx)% nx,(y+dy)% ny) for dx,dy in d] #循环边界
def getEnergyDif(state,x,y,k):
    xy=nearby(x,y)
    E0,E1=0,0
    for x_,y_ in xy:
        if state[x_,y_]==state[x,y]:
            E0-=1
        if state[x_,y_]==k:
            E1-=1
    return E1-E0
def getplot_Energy_time(steps,start_stat,q,nx,ny,beta,Low_EState=True,save=False,plot=True):
    if Low_EState:
        state=set_min_Energy_state(q)
    else:
        state=set_max_Energy_state(q)
    E=getEnergy(state)
    E_avg_list=np.zeros(steps)
    Susc_list = np.zeros(steps)
    for t in range(steps):
        # if(t>=start_stat):
        #     E_avg+= E/(nx*ny)
        #     Susc_avg += np.sum(state)/(nx*ny)-0.5
        x,y=randint(0,nx-1),randint(0,ny-1)
        NewState = randint(0,q-1)
        dif = getEnergyDif(state,x,y,NewState)
        if dif<=0 or random()<exp(-dif*beta):
            state[x,y]=NewState
            E+= dif
        E_avg_list[t] = E/(nx*ny)
        Susc_list[t]=abs(np.sum(state)/(nx*ny)-0.5) #平均磁化率
    E_avg=np.average(E_avg_list[start_stat:])
    Susc_avg=np.average(Susc_list[start_stat:])
    E_var=np.var(E_avg_list[start_stat:])
    Susc_var=np.var(Susc_list[start_stat:])
    # E_avg= data_len
    # Susc_avg/= data_len 
    if save or plot:
        plt.subplot(121)
        plt.plot(range(steps),E_avg_list)
        plt.subplot(122)
        plt.plot(range(steps),Susc_list)
    if save:
        plt.savefig("1.png")
    if plot:
        plt.show()
    ret= (1/beta,E_avg,Susc_avg,E_var,Susc_var)
    print(ret)
    return ret
def set_max_Energy_state(q=2):
    state = np.zeros((nx,ny),dtype=np.int8)
    for i in range(nx):
        for j in range(ny):
            state[i,j]= (i+j) % q
    return state
def set_min_Energy_state(q=2):
    return np.zeros((nx,ny),dtype=np.int8)

def task(*args):
    num,*args_ = args
    print(f"num {num} starts" )
    multiprocessing.Lock()
    val = getplot_Energy_time(*args_)
    return {'num':num,'result':val}
N=200
q=2
nx,ny=80,80
steps=2**20
start_stat=2**19 #100000步后开始统计

datas=[] 
if __name__ == "__main__":
    num_cores = int(multiprocessing.cpu_count())
    pool = multiprocessing.Pool(num_cores)
    results=[]
    for i in trange(N):
        T=gauss(1.2,0.16)
        if(T>0):
            # p = multiprocessing.Process(target=task,args=(steps,start_stat,q,nx,ny,1/T,True,False,False))
            t=pool.apply_async(task,args=(i,steps,start_stat,q,nx,ny,1/T,True,False,False))
            results.append(t)
    datas = [t.get()['result'] for t in results]
    print(datas)
    save_data()
    print("End.")