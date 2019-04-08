import matplotlib.pyplot as plt
import numpy as np

time = [i for i in range(0, 7)]
number = [535, 550, 545, 565, 595, 562, 600]
plt.title('Relationship between time and number')  # 创建标题
plt.xlabel('Time')  # x轴标签
plt.ylabel('Score')  # y轴标签
f = np.polyfit(time, number, 5)  # 按照最高项五次方拟合的离散系数，由泰勒公式得知越高项拟合程度越高
print("由高项往低项的系数是：")
print(f)
y = np.polyval(f, time)  # 拟合的函数
plt.plot(time, number, color='r')  # 原图红色的
plt.plot(time, y, color='b')  # 蓝色
plt.show()  # 显示
