import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

data = []
with open('LYSO.txt', 'r') as file:  # 打开txt文件
    for line in file:
        data.append(int(line.strip()))  # 将txt文件中的数据加入data中

m = 50000
sums = []
current_sum = 0
for i, num in enumerate(data, 1):
    current_sum += num
    if i % m == 0:
        sums.append(current_sum)
        current_sum = 0
# 如果列表长度不是m的整数倍，则需要额外处理最后一组数据
if current_sum != 0:
    sums.append(current_sum)

time = range(len(sums))
time1 = len(sums)
# 计算数据的平均值，作为泊松分布的期望值
lambda_ = np.mean(data)*m
poission_E = []
for i in range(time1):
    poission_E.append(lambda_)
plt.bar(time, sums, color='blue', label='sum')
plt.plot(time, poission_E, color='red', label='possion')
plt.xlabel('Time/0.1ms')
plt.ylabel('Frequency')
plt.grid(True)
plt.legend()
plt.show()