#include "math.c"
#include <stdlib.h>
#include "time.h"
#define N 10
int mod(int idx){
    if(idx<0)
        return idx+N;
    else if(idx>=N)
        return idx-N;
    else
        return idx;
}
int delta(int i,int j){
    return mod(i)== mod(j)?1:0;
}
int f(int i,int j){
    return delta(i-1,j)+delta(i+1,j)-2*delta(i,j);
}
int main(int argc,char** argv)
{
    int iter;
    if(argc == 1){
        iter=400;
    }else if(argc==2){
        iter=atoi(argv[1]);
    }else{
        printf("usage: %s [iters]",argv[0]);
    }
    double* A=(double*)malloc(N*N*sizeof(double));
    double* v =(double*)malloc(N*sizeof(double));
    double* tmp =(double*)malloc(N*sizeof(double));
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            *(A+i*N+j)=f(i,j);
        }
    }
    srand((unsigned int )time(0));
    for(int i=0; i<N; i++){
        v[i]=(double)rand()/RAND_MAX;
    }
    
    for(int i=0; i<iter; i++){
        prod(A,v,tmp,N);
        double n=norm(tmp,N);
        for(int i=0; i<N; i++){
            tmp[i]/=n;
        }
        memcpy(v,tmp,N*sizeof(double));
    }
    prod(A,v,tmp,N);
    double lambda = dot(v,tmp,N);
    printf("eigenvalue:%lf\neigenvector:\n",lambda);
    for(int i=0;i<N;i++){
        printf("%lf\n",v[i]);
    }
}