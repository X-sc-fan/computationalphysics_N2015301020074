# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 22:43:23 2017

@author: 24486
"""

from matplotlib import pyplot as plt
import numpy as np
import math

a = 10.
b = 1.
dt = 0.01
T = 100
N = N = int(T/dt) #总循环次数
print (N)
v = [0 for x in range(0,N+1)] #速度数组
t = [0 for x in range(0,N+1)] #时间数组

for i in range(N):
    v[i+1] = v[i] + (a-b*v[i])*dt
    t[i+1] = t[i] + dt

print(v[N])

x=np.linspace(0,T,1000)  #这个表示在0到10之间生成1000个x值
y=[-a/b*math.exp(-b*i)+a/b for i in x]  #对上述生成的1000个数循环用解析公式求对应的y
print(x[999])
print(y[999])
plt.plot(t,v,color='blue')
plt.plot(x,y,color='red')
plt.show()