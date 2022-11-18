from matrixCalc import SquareMatrix
dim=4
mat = [[1/(j+i+1) for j in range(dim)]for i in range(dim)]
s=SquareMatrix(mat)
a=s.Cholesky()
a.show()