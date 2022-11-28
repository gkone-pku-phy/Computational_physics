#include "math.c"
#include <memory.h>
#define SIZE 4
// #define PI 3.141592653589793
#include <stdio.h>

int main(){
    double mat[SIZE*SIZE]={1,-1,0,0,-1,2,-1,0,0,-1,3,-1,0,0,-1,4};
    
    Jacobi(mat,SIZE,30);
    show_mat(mat,SIZE);
}