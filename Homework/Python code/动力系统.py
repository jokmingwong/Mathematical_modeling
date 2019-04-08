'''
    有个医生给病人开药，要求病人血液中的钙离子浓度稳定在一个有效的值，求如何开药？
    前提：
    病人体内本身就有药物。
    在不服药的情况下，每一周的A浓度水平是前一周的一般。
    列式：
    a(n+1) = 0.5×a(n)+b
    这里为了方便画图我们先假设b=1，先画个图看看。那么式子变成：a(n+1)=0.5×a(n)+1接下来我们分别取a(0)= 1，a(0)=2,a(0)=3
    实现代码如下：
    先画a(0)=1
'''

import matplotlib.pyplot as plt


def drawCurve(Reagentperday, CurrentLevel):
    ReagentLevel = []
    for i in range(15):
        ReagentLevel.append(CurrentLevel)
        CurrentLevel = CurrentLevel * 0.5 + Reagentperday
    Time = [i for i in range(15)]
    print(Time, ReagentLevel)
    plt.plot(Time, ReagentLevel)


for i in range(1, 10):
    for j in range(1, 10):
        drawCurve(i, j)
plt.show()
