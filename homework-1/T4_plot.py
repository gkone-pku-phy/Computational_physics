from matplotlib import pyplot as plt 
import json
import math
from x2fig import get_linear_graph
n,smi=[],[]
with open("data","r") as f:
    data = json.load(f)

step = 20
cnt = 50
while cnt+step<len(data):
    avg_n,avg_smi,avg_smi_sqr = 0,0,0
    for i in range(step): #smi方差：E(x-xbar)^2 = E(x^2)-E(x)^2
        avg_n += data[cnt+i]['start']
        avg_smi += data[cnt+i]['s-i']
        avg_smi_sqr += data[cnt+i]['s-i']**2
    avg_n /= step 
    avg_smi /= step 
    avg_smi_sqr/= step 
    sigma_smi = avg_smi_sqr - avg_smi**2 
    n.append(math.log(1/avg_n))
    smi.append(math.log(math.sqrt(sigma_smi)))
    cnt+= step
get_linear_graph(n,smi,"$log(n^{-1})$","$log(\sigma(s-i))$","x","y","T4拟合.png")