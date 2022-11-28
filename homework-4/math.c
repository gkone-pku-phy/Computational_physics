#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>

#define PI 3.1415926535898
void show_mat(double* mat,size_t size);
void print_mat_latex(double* mat,size_t size);

double _getmin(double (*f)(double),double start,double stop,double prec){
    if(start>stop){
        double tmp = start;
        start=stop;
        stop=start;
    }
    const double frac= (3-sqrt(5))/2;
    double left,right,ldiv,rdiv;
    left=start,right=stop;
    ldiv = left+(right-left)*frac;
    rdiv = right-(right-left)*frac;

    while(right-left>prec){
        if(f(ldiv)>f(rdiv)){
            left=ldiv;
            // _getmin(f,ldiv,right,prec);
        } else {
            right=rdiv;
        }
        ldiv = left+(right-left)*frac;
        rdiv = right-(right-left)*frac;
    }
    return (right+left)/2;
}
double dot(double* b,double* c,size_t size){
    double s=0;
    for(int i=0;i<size;i++){
        s+= b[i]*c[i];
    }
    return s; 
}
double norm(double* b,size_t size){
    return sqrt(dot(b,b,size));
}
void prod(double* A,double* b,double* sol,size_t size){
    for(int i=0;i<size;i++){
        sol[i]=0;
        for(int j=0;j<size;j++){
            sol[i]+= *(A+size*i+j)*b[j];
        }
    }
}

void ConjGradSol(double* A,double* b,double* sol,const size_t size,double prec){
    double * r = (double*)malloc(sizeof(double)*size);
    double * p = (double*)malloc(sizeof(double)*size);
    double * Ap = (double*)malloc(sizeof(double)*size);
    prod(A,sol,r,size); // r = Ax_0
    double alpha,beta;
    for(int i=0;i<size;i++){
        r[i] = -r[i]+b[i];
        p[i]=r[i];
    }
    while (norm(r,size)>prec){
        prod(A,p,Ap,size);
        alpha = dot(r,p,size)/dot(Ap,p,size);
        for(int i=0;i<size;i++){
            sol[i]+= alpha * p[i];
            r[i] -= alpha * Ap[i];
        }
        beta = -dot(Ap,r,size)/dot(Ap,p,size);
        for(int i=0;i<size;i++){
            p[i] = r[i]+beta *p[i];
        }
    }
    free(p),free(r),free(Ap);
}


void GradDescentSol(double* A, double* b,double* sol,const size_t size,double prec){
    // sol stores initial trials.
    double* tmp = (double*)malloc(sizeof(double)*size); //tmp =  r = b-Ax
    for(int i=0;i<size;i++){
        tmp[i]=b[i];
        for(int j=0;j<size;j++){
            tmp[i]-= *(A+i*size+j)*sol[j];
        }
    }
    double alpha;
    double* tmp2= (double*)malloc(sizeof(double)*size);//tmp2 =  Ar
    while(norm(tmp,size)>prec){
        prod(A,tmp,tmp2,size);
        alpha = dot(tmp,tmp,size)/dot(tmp2,tmp,size);
        for(int i=0;i<size;i++){
            sol[i]+=alpha * tmp[i];
            tmp[i]-= alpha *tmp2[i];
        }
    }
    free(tmp);free(tmp2);
    return;
}
void matrixProd(double* A,double* B,double* sol,size_t size){
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            *(sol+i*size+j) = 0;
            for(int k=0;k<size;k++){
                *(sol+i*size+j) += *(A+i*size+k)* *(B+k*size+j);
            }
        }
    }
}

void QR_decomposition(double* mat,double* Q,double* R,size_t size){
    double* coeffs = (double*)malloc(sizeof(double)*size);

    double* rj = (double*)malloc(sizeof(double)*size);
    double* rk = (double*)malloc(sizeof(double)*size);
    for(int j=0;j<size;j++){
        for(int k=0;k<j;k++){
            for(int l=0;l<size;l++){
                rj[l] = *(mat+l*size+j);
                rk[l] = *(Q+l*size+k);
            }
            coeffs[k] = dot(rj,rk,size)/dot(rk,rk,size);
            *(R+k*size+j)=coeffs[k];
        }
        *(R+j*size+j)=1;
        for(int i=0;i<size;i++){
            *(Q+i*size+j)=*(mat+i*size+j);
            for(int k=0;k<j;k++){
                *(Q+i*size+j)-= coeffs[k]* *(Q+i*size+k);
            }
        }
    }

    double n;
    for(int j=0;j<size;j++){
        for(int i=0;i<size;i++){
            rj[i] = *(Q+i*size+j);
        }
        
        n=norm(rj,size);
        for(int i=0;i<size;i++){
            *(Q+i*size+j)/=n;
            *(R+j*size+i)*=n;
        }
    }
    free(rk),free(rj);
    return;
}
void QR_iter(double* mat,size_t size,int times){
    double* Q = (double*)malloc(sizeof(double)*size*size);
    double* R = (double*)malloc(sizeof(double)*size*size);
    memset(Q,0,sizeof(double)*size*size);
    memset(R,0,sizeof(double)*size*size);
    int cnt=0;
    while(cnt < times){
        QR_decomposition(mat,Q,R,size);
        matrixProd(R,Q,mat,size);
        cnt+=1;
        if(cnt % 5 == 0){
            printf("count=%d\n",cnt);
            print_mat_latex(mat,size);
        }

        // show_mat(Q,size);
        // show_mat(R,size);
        // show_mat(mat,size);
    }
}

void show_mat(double* mat,size_t size){
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            printf("%.4f ",*(mat+i*size+j));
        }
        printf("\n");
    }
    printf("\n");
}
void print_mat_latex(double* mat,size_t size){
    printf("\\left(\\begin{matrix}\n");
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
            printf("%.5f & ",*(mat+i*size+j));
        }
        printf("\\\\\n");
    }
    printf("\\end{matrix}\\right)\n");
    return;
}

void Givens( double* mat,size_t size,int p, int q){
    double theta;
    if(*(mat+p*size+p)==*(mat+q*size+q)){
        theta= PI/4;
    } else{
        theta = 0.5* atan(-2* *(mat+p*size+q)/(*(mat+p*size+p)-*(mat+q*size+q)));
    }
    //通过分块计算来减小计算复杂度
    if(p>=q){
        printf("warning:p>=q in Givens rotation\n");
        theta=-theta;
    }
    for(int i=0;i<size;i++){
        if(i!= p && i!= q){
            *(mat+i*size+p) = *(mat+i*size+p)*cos(theta)-*(mat+i*size+q)*sin(theta);
            *(mat+i*size+q) = *(mat+i*size+p)*sin(theta)+*(mat+i*size+q)*cos(theta);
        } 
    }
    for(int j=0;j<size;j++){
        if(j!= p && j!= q){
            *(mat+p*size+j) = *(mat+p*size+j)*cos(theta)-*(mat+q*size+j)*sin(theta);
            *(mat+q*size+j) = *(mat+p*size+j)*sin(theta)+*(mat+q*size+j)*cos(theta);
        }
    }
    double R[2][2]= {{cos(theta),sin(theta)},
    {-sin(theta),cos(theta)}};
    double RT[2][2]={{cos(theta),-sin(theta)},
    {sin(theta),cos(theta)}};
    int arr[2] = {p,q};
    double part[2][2] ={{0,0},{0,0}};
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            part[i][j]=*(mat+arr[i]*size+arr[j]);
        }
    }
    double tmp[2][2];
    matrixProd(part[0],R[0],tmp[0],2);
    matrixProd(RT[0],tmp[0],part[0],2);
    for(int i=0;i<2;i++){
        for(int j=0;j<2;j++){
            *(mat+arr[i]*size+arr[j])=part[i][j];
        }
    }
}
// void Givens_(double* mat,size_t size,int p, int q){
// 直接使用矩阵相乘计算 复杂度高
//     double* R = (double*)malloc(sizeof(double)*size*size);
//     double* RT = (double*)malloc(sizeof(double)*size*size);
//     double* temp = (double*)malloc(sizeof(double)*size*size);
//     double theta;
//     if(*(mat+p*size+p)==*(mat+q*size+q)){
//         theta= PI/4;
//     } else{
//         theta = 0.5* atan(-2* *(mat+p*size+q)/(*(mat+p*size+p)-*(mat+q*size+q)));
//     }
//     for(int i=0;i<size;i++){
//         for(int j=0;j<size;j++){
//             if(i!= p && i!= q){
//                 if(j!= p && j!= q){
//                     *(R+i*size+j) = *(RT+i*size+j) = i==j?1:0;
//                 } else{
//                     *(R+i*size+j) = *(RT+i*size+j) = 0;
//                 }
//             } else {
//                 if(j!= p && j!= q){
//                     *(R+i*size+j) = *(RT+i*size+j) = 0;
//                 } else{
                
//                     *(R+p*size+p) = *(RT+p*size+p) = cos(theta);
//                     *(R+q*size+q) = *(RT+q*size+q) = cos(theta);
//                     *(R+p*size+q)=*(RT+q*size+p) = sin(theta);
//                     *(R+q*size+p)=*(RT+p*size+q) = -sin(theta);
//                 }
//             }
//         }
//     }
//     matrixProd(mat,R,temp,size);
//     matrixProd(RT,temp,mat,size);
//     return;
// }
void Jacobi(double* mat,size_t size,int count){
    // mat为实对称矩阵
    double norm_ = 0;
    for(int i=0;i<size;i++){
        for(int j=0;j<i;j++){
            norm_ += 2*pow(fabs(*(mat+i*size+j)),2);
        }
    }
    double max_;
    int x,y;
    int cnt=0;
    while(cnt< count){
        max_=-100;
        x,y=-1,-1;
        for(int i=0;i<size;i++){
            for(int j=0;j<i;j++){
                if(fabs(*(mat+i*size+j))>max_){
                    max_= fabs(*(mat+i*size+j)) ; 
                    y=i,x=j;
                }
            }
        }
        
        // printf("i=%d, j=%d, max_=%f,norm_=%f\n",y,x,max_,norm_);
        Givens(mat,size,x,y);
        norm_=0;
        for(int i=0;i<size;i++){
            for(int j=0;j<i;j++){
                norm_ += 2*pow(fabs(*(mat+i*size+j)),2);
            }
        }
        cnt+=1;
        if(cnt % 5 == 0){
            printf("count = %d\n$$\n",cnt);
            print_mat_latex(mat,size);
            printf("$$\n");
        }
    }
}
