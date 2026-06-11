import numpy as np
import matplotlib.pyplot as plt

#参数设置
omega = 2.0    #角频率(rad/s) 
dt = 0.01      #时间步长(s)
T = 10.0       #总模拟时长(s)
N = int(T/dT)  #总步数

#初始化数组
t = np.zeros(N)     #时间
x = np.zeros(N)     #位移
v = np.zeros(N)     #速度

#初始条件
x[0] = 1.0          #初位移 (m)
v[0] = 0.0          #初速度 (m/s)

#欧拉法迭代
for i in range(N - 1):
#运动方程: dx/dt = v ,dv/dt = -omega^2 * x
a = -omega^2 * x[i] #计算当前加速度 (牛顿第二定律)
x[i + 1] = x[i] + v[i] * dt  #下一时刻位移
v[i + 1] = v[i] + a * dt     #下一时刻速度
t[i + 1] = t[i] +dt          #下一时刻时间

#绘图
plt.plot(t, x, label='数值解(欧拉法)')
plt.plot(t, x[0]*np.cos(omega*t),label='解析解(x_0cos(wt))')
plt.xlabel('时间(秒)')
plt.ylabel('位移(米)')
plt.title('简谐振动: 数值解 vs 解析解')
plt.legend()
plt.grid(True)
plt.savefig('result_plot.png', dpi=150) 
plt.show
