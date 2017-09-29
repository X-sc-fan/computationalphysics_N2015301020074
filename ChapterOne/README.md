# CHAPTER ONE

## 计算方法简介：

- 欧拉法(Euler method/forward Euler method) 是一个一阶数值解初值确定的常微分方程(ODE)的方法。欧拉法是一个一阶的数值方法，其局域误差（每一步的误差）正比于步长的平方，全局误差（在给定时间的最终误差）正比于步长。

- 以粒子衰变为例，其满足的微分方程为：

  $\frac{dN_U}{dt}=-\frac{N_U}{\tau}$

  如果我们将$N_U$在$t$作Taylor展开并忽略二阶及以上的高阶项，则有：

  $N_U(t+\Delta t)\approx N_U(t)+\frac{dN_U}{dt}\Delta t$

  根据已知的微分方程，可知：

  $N_U(t+\Delta t)\approx N_U(t)-\frac{N_U}{\tau}\Delta t$

  近似为：$N_U(t+\Delta t)\approx N_U(t)-\frac{N_U(t)}{\tau}\Delta t$

  将上式作迭代，我们可以通过数值方法得到$N_U$在某一时刻的数值。

  ​

  ## 课后练习：

  ### 1.1

  #### 源代码

  ​

  ​