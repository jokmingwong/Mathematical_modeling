import numpy as np
import matplotlib.pyplot as plt
import math as mt
c = 177257980621549879026515968
d = 293.149512426253

t = np.arange(-180000, 180000)
C1 = C2 = 293 / 2
T2 = C1 * np.exp(
    t * (55760569659390440425628128683 + 1.7633 * np.power(10, 29)) / 177257980621549879026515968) + C2 * mt.exp((
    t * (-np.sqrt(
        1.7633 * np.power(10, 29)) + 55760569659390440425628128683) / c)) - d

plt.plot(t, T2)
plt.xlim(-180000, 180000)
plt.ylim(-1.5, 1.5)

plt.xlabel("t-axis")
plt.ylabel("T2-axis")
plt.title("t-T2关系")

# Show picture
plt.show()


# 如果要存成图形
# 把 pyplot.show() 换成下面這行存储图像:
# plt.savefig("filename.png",dpi=300,format="png")
