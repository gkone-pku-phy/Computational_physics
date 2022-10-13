/*
说明：该程序用于辅助第四题中的计算，由T4.py调用。绝大多数浮点运算交由C进行，可以加快计算速度。
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))

double q_sqr = 0.5;
double sqrt_(double x){
    double ret = 0;
    if(x>= 0){
        ret = sqrt(x);
    } else {
        ret = 0;
    }
    return ret;
}
double f(double r_sqr){
    return 1/(r_sqr-q_sqr);
}
double sum_in_square(double start,double end){
    double s=0;
    double rmax,rmin,tmp=0;
    int i,j,k;
    for(i=1;i<=ceil(end);i++){
        for(j=1;j<=ceil(end);j++){
            rmax = sqrt_(pow(end,2.0)-pow(i,2.0)-pow(j,2.0));
            rmin = sqrt_(pow(start,2.0)-pow(i,2.0)-pow(j,2.0));
            for(k=MAX(ceil(rmin),1);k<ceil(rmax);k++){
                tmp += f(pow(i,2)+pow(j,2)+pow(k,2));
                // printf("%d,%d,%d,%lf\n",i,j,k,sqrt(pow(i,2)+pow(j,2)+pow(k,2)));
            }
        }
    }
    s += tmp*8;
    i=0,tmp=0;
    for(j=1;j<=ceil(end);j++){
        rmax = sqrt_(pow(end,2.0)-pow(i,2.0)-pow(j,2.0));
        rmin = sqrt_(pow(start,2.0)-pow(i,2.0)-pow(j,2.0));
        for(k=MAX(ceil(rmin),1);k<ceil(rmax);k++){
            tmp+= f(pow(i,2)+pow(j,2)+pow(k,2));
            // printf("%d,%d,%d,%lf\n",i,j,k,sqrt(pow(i,2.0)+pow(j,2.0)+pow(k,2.0)));
        }
    }
    s+= tmp * 12;
    i=0,j=0;
    tmp=0;
    rmax = sqrt_(pow(end,2.0)-pow(i,2.0)-pow(j,2.0));
    rmin = sqrt_(pow(start,2.0)-pow(i,2.0)-pow(j,2.0));
    for(k=MAX(ceil(rmin),1);k<ceil(rmax);k++){
        tmp+= f(pow(i,2)+pow(j,2)+pow(k,2));
        // printf("%d,%d,%d,%lf\n",i,j,k,sqrt(pow(i,2.0)+pow(j,2.0)+pow(k,2.0)));
    }
    s+= tmp * 6;
    if(fabs(start-0)<1e-5){
        s+= f(0);
    }
    return s;
}

int main(int argc, char *argv[]){
    if(argc == 3){
        double start = atof(argv[1]);
        double end = atof(argv[2]);
        // printf("%lf\n,%lf\n", start, end);
        double res = sum_in_square(start, end);
        printf("%.15lf\n",res);
    }else{
        printf("Not correct");
        return -1;
    }
    
    return 0;
}