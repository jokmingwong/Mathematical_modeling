# 蒙特卡罗方法的定积分模拟

import random


# 在此处更改方程即可
def func(x):
    return x


n = int(input("The number of random you want to input:\n"))
t1 = float(input("The lower boundary:\n"))
t2 = float(input("The upper boundary\n"))
upper = float(input("The upper boundary of this function\n"))
count = 0

for i in range(0, n):
    x = t1 + random.random() * (t2 - t1)
    y = upper * random.random()
    if y <= func(x):
        count += 1

result = float(float(count / n) * (t2 - t1) * upper)
error = result/
print(result)

