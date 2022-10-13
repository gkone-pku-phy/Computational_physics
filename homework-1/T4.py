import sys
from math import *
import signal
import json
import os 


q=sqrt(0.5)
q_sqr = q**2

def g(r_sqr):
    return 1/(r_sqr-q_sqr)
def h(r_sqr):
    return -1/12* (2*r_sqr+6*q_sqr)/(r_sqr-q_sqr)**3
def sqrt_(x):
    return sqrt(x) if x>=0 else 0
def sum_in_sphere(f,r0,r):
    '''
    计算r0到r的球壳内计算所有点处的f(x)的和
    sum over r>=r0 and r<=r
    '''
    s = 0
    for i in range(1,ceil(r)+1):
        for j in range(1,ceil(r)+1):
            rmax=sqrt_(r**2-i**2-j**2)
            rmin = sqrt_(r0**2-i**2-j**2)
            for k in range(max(ceil(rmin),1),ceil(rmax)):
                s+= f(i**2+j**2+k**2)*8
                # print(i,j,k,sqrt(i**2+j**2+k**2))
    i=0
    for j in range(1,ceil(r)+1):
        rmax=sqrt_(r**2-i**2-j**2)
        rmin = sqrt_(r0**2-i**2-j**2)
        for k in range(max(ceil(rmin),1),ceil(rmax)):
            s+= f(i**2+j**2+k**2)*12
    i,j=0,0
    rmax=sqrt_(r**2-i**2-j**2)
    rmin = sqrt_(r0**2-i**2-j**2)
    for k in range(max(ceil(rmin),1),ceil(rmax)):
        s+= f(i**2+j**2+k**2)*6
    if r0==0: 
        s+=f(0)
    return s
def direct_integration(Lambda):
    return 4*pi*Lambda + 2*pi*q*(log((Lambda-q)/(Lambda+q)))
def cprog(start,stop):
    a=os.popen("T4_Cprog.exe {} {}".format(start,stop))
    try:
        f=float(a.readline())
    except ValueError as e:
        print(e)
        print(a.readlines())
        with open(filename,"w") as f:
            json.dump(datas,f)
        print("saved.Program exit.")
        exit(1)
    return f
filename="data"
def sigint_handler(signum, frame):
    print('SIGINT received. Program shutting down. Saving data.')
    with open(filename,"w") as f:
        json.dump(datas,f)
    print("saved.")
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
if __name__=="__main__":
    if os.path.exists(filename):
        with open(filename,'r') as f:
            datas = json.load(f)
            start=datas[-1]['start']
            s=datas[-1]['sum']
    else:
        datas=[]
        start=0.1
        s=sum_in_sphere(g,0,start)
    step=1
    radius = start 
    print(f"init:start={start},step:{step},sum={s}")
    while True:
        print(f"radius={radius},approximately {round(4*pi*radius**2)} points.")
        # s,radius = s+sum_in_sphere(g,radius,radius+step),radius+step
        s,radius = s+cprog(radius,radius+step),radius+step
        int_ = direct_integration(radius)
        print(f"sum:{s},integral:{int_},sum-integral={s-int_}")
        datas.append({'start':radius,'sum':s,'integral':int_,'s-i':s-int_})