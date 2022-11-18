---
mode: passage
---
# 偏微分方程的求解

1. 按自变量个数：
- 常微分方程
- 偏微分方程

2. 按边界：
- 初值问题：给出解在某一点的状态
- 边值问题： 给出解在至少两点的状态

$$
\frac{d^2y}{dx^2} =f(x,y,y') \\ 
a_0y(a)+b_0y'(a)=r_0 \\ 
a_1y(b)+b_1y'(b) = r_1 \\ 
$$
边界条件：
1. 第一类：$b_0=b_1=0$(Direchlet) 
2. 第二类：$a_0=a_1=0$(Neumann)
3. 第三类：混合(Robinns)

## 欧拉法（差分）
以
$$
u'(t) = f(t,u),\\ 
u(a) = u_0
$$

为例，划分为$n+1$个节点：$\{t_k\},k=1,2,\cdots,n+1$
step size: $h=\rm dt = (b-a)/n$
记$u_k = u(t_k),u_k' = u'(t_k)$

### 向前差商近似：
$$
u_k' = u'(t_k ) \approx [u_{k+1}-u_k ]/h \Rightarrow u_{k+1} \approx u_k + hf(t_k,u_k)
$$
### 向后差商近似：
$$
u'_{k+1} \approx [u_{k+1}-u_k]/h \Rightarrow u_{k+1}\approx u_k + hf(t_{k+1},u_{k+1})
$$

### 两步法

$$
u_k'\approx [u_{k+1}-u_{k-1}]/2h \Rightarrow u_{k+1}\approx u_{k-1} +2hf(t_k,u_k)
$$
上式是显式的。$u_2$需要特别处理。$u_2 \approx u_1 + hf(t_1,u_1)$
### 积分近似：
$$
u_{k+1} \approx u_k +\int_{t_k}^{t_{k+1}} f(t,u)\rm dt \\ 
u_{k+1} \approx u_k+\frac{h}{2}[f(t_k,u_k)+f(t_{k+1},u_{k+1})]
$$


$$

$$
