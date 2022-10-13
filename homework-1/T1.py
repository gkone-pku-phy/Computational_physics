from math import *

maxn = 100
def simpleExpansionExp(x):
    result = 0
    for n in range(maxn):
        result += (-1)**n *x**n/factorial(n)
    return result 
def recursionExp(x):
    '''
    e^{-x} = \sum_{n=0}^\infty s_n = 
    '''
    s=1
    result = 0
    for n in range(1,maxn):
        result+=s
        s*=(-1)*x/n
    return result 
def invRecursionExp(x): 
    s=1 
    result = 0 
    for n in range(1,maxn):
        result += s
        s*=x/n 
    return 1/result

for x in range(0,20,2):
    print(x,simpleExpansionExp(x),recursionExp(x),invRecursionExp(x),exp(-x))
