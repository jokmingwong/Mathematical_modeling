import numpy as np


def tryExample():
    # 生成一个0到5的整数顺序序列
    a = np.arange(5)

    print("多于一维的:")
    a = np.array([np.arange(2), np.arange(2)])
    print(a)

    print("最小维度:")
    b = np.array([1, 2, 3, 4, 5], ndmin=2)
    print(b)

    print("复数形式:")
    c = np.array([1, 2, 3, 4, 5], dtype=complex)
    print(c)

    print("使用数组标量类型:")
    dt = np.dtype(np.int64)
    print(dt)

    print("应用结构化数据类型:")
    # 说明这是一个多属性数组，类似结构体
    # 比如下面age说明属性名，np.int8是属性的数据类型
    dt = np.dtype([('age', np.int8)])
    # 数字后面还加逗号说明这是一个向量
    e = np.array([(10,), (20,), (30,)], dtype=dt)
    print(e)
    print("文件名称可访问age列的内容")
    dt = np.dtype([('age', np.int8)])
    A = np.array([(10,), (20,), (30,)], dtype=dt)
    print(A['age'])

    # Example
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    g = np.array([('Adam', 19, 100), ('Marry', 21, 98), ('Catty', 20, 81)])
    print(g)

    # 输出数组规模
    g = np.array([[1, 2, 3], [4, 5, 6]])
    print(g.shape)
    # 也可以通过更改shape使得数组规模改变，但数组大小不变
    g.shape = (3, 2)
    print(g)

    # 通过arrange(n)方法可以将数从0到n填满，ndim返回维度
    a = np.arange(24)
    print("其维度为:")
    print(a.ndim)
    print("其flags属性返回其一堆风格判定值:")
    print(a.flags)
    b = a.reshape(2, 4, 3)
    # 现在为2*4*3矩阵
    print(b)
