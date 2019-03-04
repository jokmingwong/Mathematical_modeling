import numpy as np

# 随机创建,第一个参数为shape，第二个参数为数据类型，第三个为排序风格
x = np.empty([3, 2], dtype=int)
print(x)

# 用0初始化
y = np.zeros([3, 2], dtype=float, order='C')
print(y)
# 同样可以用ones初始化
z = np.ones([3, 3], dtype=int, order="C")
print(z)

# 也可以用asarray()将已知数组或者元组转换成array
x = [i * i for i in range(1, 11)]
t = np.asarray(x, dtype=int, order='C')
q = t.reshape(5, 2)
print(q)

print("即使不是很正常的数组也能初始化")
x = [(1, 2, 3), (5, 11)]
print(np.asarray(x))
# arrange()有四个参数，分别为start,end,step,datatype
print(np.arange(3, 12, 2, dtype=float))
# 切片方法,第三个参数是指将这个数组分割成多少份
print(np.linspace(10, 20, 5, endpoint=True))

# 对数函数的输出
print(np.logspace(1.0, 5.0, base=20, num=5, dtype=int))
