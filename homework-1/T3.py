from torch import cholesky
from matrixCalc import SquareMatrix
def get_by_C(matrix,b):
    ret = matrix.Cholesky()
    rett = ret.transverse()
    # ret.show()
    # rett.show()
    sol = SquareMatrix.Backward_(rett,b)
    # print(sol)
    solutions = SquareMatrix.Backward(ret,sol)
    return solutions
def get_by_GEM(matrix,b):
    ret,b_=matrix.GEM(b)
    # ret.show()
    # print(b_)
    solutions = SquareMatrix.Backward(ret,b_)
    return solutions
for n in range(1,11):
    print(f"n={n}")
    
    mat = [[0 if (i==0 or j==0) else (1/(i+j-1)) for i in range(n+1)] for j in range(n+1)]
    b = [0 if i==0 else 1 for i in range(n+1)]
    matrix = SquareMatrix(mat)

    solutions = get_by_C(matrix,b)
    for i in range(1,n+1):
        print(f"Cholesky sol {i}:{solutions[i]}")
    solutions = get_by_GEM(matrix,b)
    for i in range(1,n+1):
        print(f"GEM sol {i}:{solutions[i]}")
    

    
    
    