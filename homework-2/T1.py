from matrixCalc import SquareMatrix
def get_by_C(matrix,b):
    ret = matrix.Cholesky()
    print("Cholesky消元法得到的矩阵：")
    print(ret)
    rett = ret.transverse()
    sol = SquareMatrix.Backward_(rett,b)
    solutions = SquareMatrix.Backward(ret,sol)
    return solutions
def get_by_GEM(matrix,b):
    ret,b_=matrix.GEM(b)
    solutions = SquareMatrix.Backward(ret,b_)
    return solutions
if __name__=="__main__":
    m = SquareMatrix([[0.05,0.07,0.06,0.05],[0.07,0.10,0.08,0.07],[0.06,0.08,0.10,0.09],[0.05,0.07,0.09,0.10]])
    b=[0.23,0.32,0.33,0.31]
    print(get_by_C(m,b))
    print(get_by_GEM(m,b))