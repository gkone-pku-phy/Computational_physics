#define SIZE 4
#include "math.c"

int main(){
    double a[SIZE][SIZE] ={
        {0.05,0.07,0.06,0.05},
        {0.07,0.10,0.08,0.07},
        {0.06,0.08,0.10,0.09},
        {0.05,0.07,0.09,0.10}
    };
    double b[SIZE] = {0.23,0.32,0.33,0.31};
    double sol[SIZE] = {0,0,0,0};
    GradDescentSol(*a,b,sol,SIZE,1e-9);
    for(int i=0;i<SIZE;i++){
        printf("%f ",sol[i]);
    }
    printf("\n");

    for(int i=0;i<SIZE;i++) 
        sol[i]=0;

    ConjGradSol(*a,b,sol,SIZE,1e-9);
    for(int i=0;i<SIZE;i++){
        printf("%f ",sol[i]);
    }
    return 0;
}