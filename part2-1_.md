  
  
<style>.title_passage {
  background-color: #1cd0f0;
  font-size: 50px;
  font-weight: bold;
  padding-left: 5px;
  border-radius: 5px;
}
@media print {
  .markdown-preview {
    width: 97%;
  }
  .markdown-preview h1,
  .markdown-preview h2,
  .markdown-preview h3,
  .markdown-preview h4,
  .markdown-preview h5,
  .markdown-preview h6 {
    font-weight: 400;
  }
  .markdown-preview h1 {
    font-size: 24px;
  }
  .markdown-preview h2 {
    font-size: 22px;
  }
  .markdown-preview h3 {
    font-size: 20px;
  }
  .markdown-preview h4 {
    font-size: 16px;
  }
}
h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 400;
}
h1 {
  font-size: 24px;
}
h2 {
  font-size: 22px;
}
h3 {
  font-size: 20px;
}
h4 {
  font-size: 16px;
}
body {
  font-size: 14px;
  background-size: cover;
  width: 100%;
  height: 100%;
  background-repeat: repeat;
  min-height: 100%;
}
h1 {
  font-size: 40px !important;
  color: whitesmoke;
  background-color: #8b0012;
  height: 50px;
}
.title2 {
  font-size: 60px !important;
  background-color: #f2647b;
  height: 10%;
}
.title3 {
  font-size: 48px !important;
  background-color: #51ff00;
  height: 8%;
}
.title4 {
  font-size: 36px !important;
  background-color: #d5b732;
  height: 7%;
}
</style>
  
  
  
  
#  偏微分方程的求解
  
  
1. 按自变量个数：
- 常微分方程
- 偏微分方程
  
2. 按边界：
- 初值问题：给出解在某一点的状态
- 边值问题： 给出解在至少两点的状态
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?&#x5C;frac{d^2y}{dx^2}%20=f(x,y,y&#x27;)%20&#x5C;&#x5C;%20a_0y(a)+b_0y&#x27;(a)=r_0%20&#x5C;&#x5C;%20a_1y(b)+b_1y&#x27;(b)%20=%20r_1%20&#x5C;&#x5C;"/></p>  
  
边界条件：
1. 第一类：<img src="https://latex.codecogs.com/gif.latex?b_0=b_1=0"/>(Direchlet) 
2. 第二类：<img src="https://latex.codecogs.com/gif.latex?a_0=a_1=0"/>(Neumann)
3. 第三类：混合(Robinns)
  
##  欧拉法（差分）
  
以
<p align="center"><img src="https://latex.codecogs.com/gif.latex?u&#x27;(t)%20=%20f(t,u),&#x5C;&#x5C;%20u(a)%20=%20u_0"/></p>  
  
  
为例，划分为<img src="https://latex.codecogs.com/gif.latex?n+1"/>个节点：<img src="https://latex.codecogs.com/gif.latex?&#x5C;{t_k&#x5C;},k=1,2,&#x5C;cdots,n+1"/>
step size: <img src="https://latex.codecogs.com/gif.latex?h=&#x5C;mathrm%20dt%20=%20(b-a)&#x2F;n"/>
记<img src="https://latex.codecogs.com/gif.latex?u_k%20=%20u(t_k),u_k&#x27;%20=%20u&#x27;(t_k)"/>
  
###  向前差商近似：
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?u_k&#x27;%20=%20u&#x27;(t_k%20)%20&#x5C;approx%20[u_{k+1}-u_k%20]&#x2F;h%20&#x5C;Rightarrow%20u_{k+1}%20&#x5C;approx%20u_k%20+%20hf(t_k,u_k)"/></p>  
  
###  向后差商近似：
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?u&#x27;_{k+1}%20&#x5C;approx%20[u_{k+1}-u_k]&#x2F;h%20&#x5C;Rightarrow%20u_{k+1}&#x5C;approx%20u_k%20+%20hf(t_{k+1},u_{k+1})"/></p>  
  
  
###  两步法
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?u_k&#x27;&#x5C;approx%20[u_{k+1}-u_{k-1}]&#x2F;2h%20&#x5C;Rightarrow%20u_{k+1}&#x5C;approx%20u_{k-1}%20+2hf(t_k,u_k)"/></p>  
  
上式是显式的。<img src="https://latex.codecogs.com/gif.latex?u_2"/>需要特别处理。<img src="https://latex.codecogs.com/gif.latex?u_2%20&#x5C;approx%20u_1%20+%20hf(t_1,u_1)"/>
###  积分近似：
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?u_{k+1}%20&#x5C;approx%20u_k%20+&#x5C;int_{t_k}^{t_{k+1}}%20f(t,u)&#x5C;mathrm%20dt%20&#x5C;&#x5C;%20u_{k+1}%20&#x5C;approx%20u_k+&#x5C;frac{h}{2}[f(t_k,u_k)+f(t_{k+1},u_{k+1})]"/></p>  
  
  
<div class="def" name=object Object  style="">
123
</div>
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?"/></p>  
  
  