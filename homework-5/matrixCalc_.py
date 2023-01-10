from copy import deepcopy
from math import sqrt
class SquareMatrix:
    @classmethod
    def fromZero(cls,m):
        _matrix = [[0 for _ in range (m)] for __ in range(m)]
        return cls(_matrix)
    def __init__(self,mat):
        self.m = len(mat)
        self._matrix = [[0 for _ in range(self.m)] for __ in range(self.m)]
        for i in range(self.m):
            for j in range(self.m):
                self._matrix[i][j] = mat[i][j]
        # print(self._matrix)
    @classmethod
    def Backward(cls,upTriangular,b):
        m=upTriangular.m
        assert(len(b)==m)
        solutions=[0 for i in range(m)]
        for i in range(m-1,-1,-1):
            if upTriangular._matrix[i][i] == 0:
                print("Warning: the matrix is singular!!!")
                exit(1)
            solutions[i]=b[i]
            for j in range(m-1,i-1,-1):
                solutions[i]-=upTriangular._matrix[i][j]*solutions[j]
            solutions[i]/=upTriangular._matrix[i][i]
        return solutions[:]
    @classmethod
    def Backward_(cls,downTriangular,b):
        
        m=downTriangular.m
        assert(len(b)==m)
        solutions=[0 for i in range(m)]
        for i in range(m):
            if downTriangular._matrix[i][i] == 0:
                print("Warning: the matrix is singular!!!")
                exit(1)
            solutions[i]=b[i]
            for j in range(i):
                solutions[i]-=downTriangular._matrix[i][j]*solutions[j]
            solutions[i]/=downTriangular._matrix[i][i]
        return solutions[:]


    def transverse(self):
        ret = SquareMatrix.fromZero(self.m)
        for i in range(self.m):
            for j in range(self.m):
                ret._matrix[i][j]=self._matrix[j][i]
        return ret



    def GEM(self,b):
        assert(len(b)==self.m)
        ret = deepcopy(self._matrix)
        
        for l in range(self.m):
            for k in range(l+1,self.m):
                ret_kl=ret[k][l]
                ret[k][l]=0
                for i in range(l+1,self.m):
                    ret[k][i]-=ret[l][i]*ret_kl/ret[l][l]
                b[k]-= b[l]*ret_kl/ret[l][l]
        ret = [[ret[i][j] for j in range(self.m)] for i in range(self.m)]
        return SquareMatrix(ret),b[:]
    def Cholesky(self):
        # assert(len(b) == self.m)
        # b=[0]+b
        n=self.m
        ret =[ [0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for k in range(i-1):
                tmp = self._matrix[k][i]
                for l in range(k-1):
                    tmp -= ret[l][i]*ret[l][k]
                ret[k][i] = tmp / ret[k][k]
            tmp = self._matrix[i][i]
            for k in range(i-1):
                tmp -= ret[k][i]**2 
            ret[i][i]=sqrt(tmp)
        ret = [[ret[i][j] for j in range(self.m)] for i in range(self.m)]
        return SquareMatrix(ret)
    def product(self,b):
        ret= [0 for i in range(self.m)]
        for i in range(self.m):
            ret[i] = sum([self._matrix[i][k]*b[k] for k in range(self.m)])
        return ret
    def show(self):
        for i in range(self.m):
            for j in range(self.m):
                print("%.8f"%self._matrix[i][j],'\t\t',end='')
            print()
    def __repr__(self):
        ret = ""
        for i in range(self.m):
            for j in range(self.m):
                ret+="{:+.8f}  ".format( self._matrix[i][j])
            ret+='\n'
        return ret
def get_by_GEM(matrix,b):
    ret,b_=matrix.GEM(b)
    solutions = SquareMatrix.Backward(ret,b_)
    return solutions