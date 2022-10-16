from matrixCalc import SquareMatrix
from T1 import get_by_GEM
def cubic_spline_interpolation(f,xs):
    length = len(xs)-1 # len xs == n+1
    a,b,c,d=[0 for i in range(length)],[0 for i in range(length)],\
        [0 for i in range(length)],[0 for i in range(length)]
    y= [f(x) for x in xs] #len==n+1
    h = [xs[i+1]-xs[i] for i in range(length)] #len == n
    g = [(y[i+1]-y[i])/h[i] for i in range(length)] # len == n
    mat = [[0 for j in range(length+1)] for i in range(length+1)]
    b_ = [0 for i in range(length+1)]
    # fill in the matrix elements.
    for i in range(length+1):
        if i == 0 or i == length:
            mat[i][i]=1
            b_[i]=0
            continue
        else:
            mat[i][i-1]=h[i-1]
            mat[i][i]=2*(h[i-1]+h[i])
            mat[i][i+1]=h[i]
            b_[i]=3*(g[i]-g[i-1])
        
    m = SquareMatrix(mat)
    
    solutions = get_by_GEM(m,b_)
    for i in range(length):
        c[i]=solutions[i]
        d[i]=(solutions[i+1]-solutions[i])/(3*h[i])
        b[i]=g[i]-c[i]*h[i]-d[i]*h[i]**2
        a[i]=y[i]
    def f(x:float) -> float:
        for i in range(length):
            if (x<=xs[i+1] and x>=xs[i]):
                return a[i]+b[i]*(x-xs[i])+c[i]*(x-xs[i])**2+d[i]*(x-xs[i])**3 
        raise Warning("function out of range!")
    return a,b,c,d,f