from copy import deepcopy
from math import sqrt
class SquareMatrix:
    @classmethod
    def fromZero(cls,m):
        _matrix = [[0 for _ in range (m)] for __ in range(m)]
        return cls(_matrix)
    def __init__(self,mat):
        self.m = len(mat)
        self._matrix = [[0 for _ in range(self.m+1)] for __ in range(self.m+1)]
        for i in range(1,self.m+1):
            for j in range(1,self.m+1):
                self._matrix[i][j] = mat[i-1][j-1]
        # print(self._matrix)
    @classmethod
    def Backward(cls,upTriangular,b):
        m=upTriangular.m
        assert(len(b)==m)
        b=[0]+b
        solutions=[0 for i in range(m+1)]
        for i in range(m,0,-1):
            if upTriangular._matrix[i][i] == 0:
                print("Warning: the matrix is singular!!!")
                exit(1)
            solutions[i]=b[i]
            for j in range(m,i,-1):
                solutions[i]-=upTriangular._matrix[i][j]*solutions[j]
            solutions[i]/=upTriangular._matrix[i][i]
        return solutions[1:]
    @classmethod
    def Backward_(cls,downTriangular,b):
        
        m=downTriangular.m
        assert(len(b)==m)
        b=[0]+b
        solutions=[0 for i in range(m+1)]
        for i in range(1,m+1):
            if downTriangular._matrix[i][i] == 0:
                print("Warning: the matrix is singular!!!")
                exit(1)
            solutions[i]=b[i]
            for j in range(1,i):
                solutions[i]-=downTriangular._matrix[i][j]*solutions[j]
            solutions[i]/=downTriangular._matrix[i][i]
        return solutions[1:]


    def transverse(self):
        ret = SquareMatrix.fromZero(self.m)
        for i in range(1,self.m+1):
            for j in range(1,self.m+1):
                ret._matrix[i][j]=self._matrix[j][i]
        return ret



    def GEM(self,b):
        assert(len(b)==self.m)
        b=[0]+b
        ret = deepcopy(self._matrix)
        
        for l in range(1,self.m+1):
            for k in range(l+1,self.m+1):
                ret_kl=ret[k][l]
                ret[k][l]=0
                for i in range(l+1,self.m+1):
                    ret[k][i]-=ret[l][i]*ret_kl/ret[l][l]
                b[k]-= b[l]*ret_kl/ret[l][l]
        ret = [[ret[i][j] for j in range(1,self.m+1)] for i in range(1,self.m+1)]
        return SquareMatrix(ret),b[1:]
    def Cholesky(self):
        # assert(len(b) == self.m)
        # b=[0]+b
        n=self.m
        ret =[ [0 for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n+1):
            for k in range(1,i):
                tmp = self._matrix[k][i]
                for l in range(1,k):
                    tmp -= ret[l][i]*ret[l][k]
                ret[k][i] = tmp / ret[k][k]
            tmp = self._matrix[i][i]
            for k in range(1,i):
                tmp -= ret[k][i]**2 
            ret[i][i]=sqrt(tmp)
        ret = [[ret[i][j] for j in range(1,self.m+1)] for i in range(1,self.m+1)]
        return SquareMatrix(ret)
    def product(self,b):
        ret= [0 for i in range(self.m+1)]
        for i in range(1,self.m+1):
            ret[i] = sum([self._matrix[i][k]*b[k] for k in range(1,self.m+1)])
        return ret
        # for j in range(1,n+1):
        #     for k in range(1,j):
        #         ret[j][j]-=ret[j][k]**2 
        #     ret[j][j]= ret[j][j]**0.5 
        #     for i in range(j+1,n+1):
        #         for k in range(1,j):
        #             ret[i][j]-=ret[i][k]*ret[j][k]
        #         ret[i][j]/= ret[j][j]
        return ret
    def show(self):
        for i in range(1,self.m+1):
            for j in range(1,self.m+1):
                print("%.8f"%self._matrix[i][j],'\t\t',end='')
            print()
    def __repr__(self):
        ret = ""
        for i in range(1,self.m+1):
            for j in range(1,self.m+1):
                ret+="{:+.8f}  ".format( self._matrix[i][j])
            ret+='\n'
        return ret
def get_by_GEM(matrix,b):
    ret,b_=matrix.GEM(b)
    solutions = SquareMatrix.Backward(ret,b_)
    return solutions