 # Numpy笔记

 > 数据分析是Python的杀手锏

 不管如何先这样引入numpy包
```python
import numpy as np
```

### 生成一个0到5的整数顺序序列
```py
    a = np.arange(5)
```

### 多于一维的:
```python
    a = np.array([np.arange(2), np.arange(2)])
    print(a)
```

### 最小维度:
```python
    b = np.array([1, 2, 3, 4, 5], ndmin=2)
```

### 复数形式:
```python
c = np.array([1, 2, 3, 4, 5], dtype=complex)
```

### 使用数组标量类型:
```python
    dt = np.dtype(np.int64)
```


### 应用结构化数据类型:
说明这是一个多属性数组，类似结构体
比如下面age说明属性名，np.int8是属性的数据类型
>   数字后面还加逗号说明这是一个向量
```py    
dt = np.dtype([('age', np.int8)])
    e = np.array([(10,), (20,), (30,)], dtype=dt)
    print(e)
```

### 文件名称可访问age列的内容
```py
    dt = np.dtype([('age', np.int8)])
    A = np.array([(10,), (20,), (30,)], dtype=dt)
    print(A['age'])

```

### Example
```py
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    g = np.array([('Adam', 19, 100), ('Marry', 21, 98), ('Catty', 20, 81)])
```

### 输出数组规模
```py
    g = np.array([[1, 2, 3], [4, 5, 6]])
    print(g.shape)
```
###  也可以通过更改shape使得数组规模改变，但数组大小不变,若企图改变数组大小则会报错
```py
    g.shape = (3, 2)
    print(g)
```
### 通过arrange(n)方法可以将数从0到n填满，ndim返回维度
```py
    a = np.arange(24)
    print("其维度为:")
    print(a.ndim)
    print("其flags属性返回其一堆风格判定值:")
    print(a.flags)
    b = a.reshape(2, 4, 3)
    # 现在为2*4*3矩阵
    print(b)
```

### 从多维变回一维

##### 有两个类似的处理函数
1. `ravel()`返回的只是视图不会分配内存
```python
    a = np.array[1,2,3,4,5,6]
    b = np.reshape(2,3)
    print(b.ravel)
```
2. `flatten()`函数便会分配内存

##### 改变`shape`

1. `reshape()`只返回视图
2. `resize()`是确定改变原数组容量
3. `transpose()`返回矩阵的转置,`T`为其的不同名函数

##### numpy解线性方程

注意`mat()`函数的使用方法，这里的`mat`是matrix的简称

```python
A = np.mat("1 2 3;6 7 9;2 4 3")
b = np.array([1,2,3])
x = np.linalg.solve(A,b)
```

