import numpy as np

print("当a,b有一方是多维数组的时候展开为一维数组:")
a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
print(np.vdot(a,b))

print("而Numpy中有内积的运算不同于上面的点积:")
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.inner(a,b))

