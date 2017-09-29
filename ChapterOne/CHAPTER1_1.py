from matplotlib import pyplot as plt
import numpy as np

g = 9.8 #定义重力加速度的值
dt = 0.001 #定义步长
N = int(10/dt) #总循环次数
v = [0 for x in range(0,N+1)] #速度数组
t = [0 for x in range(0,N+1)] #时间数组
#print (len(v))

for i in range(N):
    v[i+1] = v[i] - g*dt #利用微分方程求解
    t[i+1] = t[i] + dt
 #   print(v[i+1])

x=np.linspace(0,10,1000)  #这个表示在0到10之间生成1000个x值
y=[-g*i for i in x]  #对上述生成的1000个数循环用解析公式求对应的y

print (v[N])

plt.plot(t,v,color='blue') #绘出数值解的图像
plt.plot(x,y,color='red')  #绘出解析解的图像
plt.show()