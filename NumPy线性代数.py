import numpy as np

'''运用的是numpy里面的linalg包'''

A = np.mat("1 5;-2 -7")
# 上面的双引号里面吗不要加多余的分号
b = np.array([7, -5])
x = np.linalg.solve(A, b)
print(x)
print("\n")

# 也可以将b换成一个矩阵
A = np.mat("1 0; 0 2")
b = np.array([[2, 0], [0, 4]])
x = np.linalg.solve(A, b)
print(x)
print("\n")

# 求逆运算
B = np.mat("1 3 5; 0 2 6; 0 0 1")
print(np.linalg.inv(B))
print("\n")

# 对数组内部属性研究
number = [1, 2, 3, 4, 5, 6, 7]
print(np.max(number))
print(np.min(number))
print(np.mean(number))
# std是标准差
print(np.std(number))
print(np.median(number))

# 求特征值
print(np.linalg.eigvals(A))
# 返回一个array表示特征值，一个matrix表示特征向量
print(np.linalg.eig(A))