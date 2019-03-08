# 第一次作业

## 摘要

##背景

## 模型假设

  (扯一下仆人下不下船的临界条件)

## 模型建立

##### 建模

提出假设：（以商人数是3人为例）

1. 商人和仆人从北岸出发，目的地是南岸

2. `mer`表示某次运送前北岸商人的人数，`ser`表示某次运送前仆人的人数

3. `mnext`和`snext`分别表示某次运送后北岸商人的数量，北岸仆人的数量

   则运送过程中需要满足以下的条件（state向量的意义见“模型中的逻辑结构”）

   （1）![img](file:///C:\Users\yogurt\AppData\Local\Temp\ksohtml7016\wps1.png)

   （2）![img](file:///C:\Users\yogurt\AppData\Local\Temp\ksohtml7016\wps2.png)

   （3）![img](file:///C:\Users\yogurt\AppData\Local\Temp\ksohtml7016\wps3.png)

##### 模型：无向图结构模型

***建模思路***

| 概念模型                                       | 逻辑模型                          | 抽象模型                       |
| ---------------------------------------------- | --------------------------------- | ------------------------------ |
| 北岸人数与运送人数的方案（由条件检查确保可行） | 二维向量grid的索引，before，after | 无向图结构中的点               |
| 运送方案                                       | 二维向量`grid[before][after]`     | 无向图结构中的边               |
| 可运送的商人与仆人人数组合                     | 两个一维向量，cmer，cser          | 无向图结构中边上允许的流量流动 |



***模型中的逻辑结构***



1. 使用二维向量state 和 grid 的数据结构（以商人数量3为例）

| 仆人 \| 商人 | 0    | 1    | 2    | 3    |
| ------------ | ---- | ---- | ---- | ---- |
| 0            | 1    | 0    | 0    | 1    |
| 1            | 1    | 1    | 0    | 1    |
| 2            | 1    | 0    | 1    | 1    |
| 3            | 1    | 0    | 0    | 1    |

​										表1：二维向量state

布尔值二维向量state，描述北岸（出发岸）商人和仆人人数的可行解，如：商人1人，仆人1人，可行表示为1；如：商人2人，仆人1人，则对岸商人1人，仆人两人，不满足条件，不可行表示为0。

| 0    | 0    | 0    | 0    |
| ---- | ---- | ---- | ---- |
| 0    | 0    | 0    | 0    |
| 0    | 0    | 0    | 0    |
| 0    | 0    | 0    | 0    |

​                                                                               表2：二维向量grid

布尔值二维向量grid，描述北岸（出发岸）人数与运走人数之间的方案（可行性由条件判断确定），即**无向图结构的邻接矩阵**，如向量值`grid[before][after] == grid[after][before] == 1`,则证明已访问过图中该点。

当满足上述的三条条件之后，标记这一点已经被访问过，也就是当前这种出发人数与运走人数的状态已经被访问（加入到了运送方案中），再递归调用这一点的邻接节点。

```java
if (mnext >= 0 && mnext < num + 1 && snext >= 0 && snext < num + 1 && state[mnext][snext])
			{
				int after = mnext * (num + 1) + snext;
				if (!grid[before][after] && !grid[after][before])
				{
					grid[before][after] = 1;
					grid[after][before] = 1;
					DFS(mnext, snext, step + 1, !dir);
					grid[before][after] = 0;
					grid[before][after] = 0;
				}
			}
		}
```



2. 使用一维向量cmer,cser表示允许的可转移集合，即，每次可运送的人数，由两个向量的index匹配，如cmer[0],cser[0]表示一次允许的可转移集合，可转移两个商人和0个仆人（满足运送要求）

   ```java
   int cmer[5] = { 2, 1, 0, 1, 0 };
   int cser[5] = { 0, 1, 2, 0, 1 };
   ```

   

3. 使用一维向量mstep,sstep记录每次的运送情况，程序最后输出这两个向量中的内容即可得到运送方案

   ```java
   int mstep[maxn*maxn];
   int sstep[maxn*maxn];
   ```

   

4. 使用布尔值dir表示运送的方向，按照假设，dir = true, 表示从北岸运送到南岸，dir = false,表示从南岸运送到北岸

   ```java
   bool dir = false;
   ```

5. 运用算法：深度优先搜索遍历二维向量grid,即无向图结构的邻接矩阵，根据运送方向的不同分类讨论

   （1）递归出口：已经到达最终状态，即北岸的商人和仆人的人数都是0

   输出mstep，sstep向量中保存的运送方案

   ```java
   if (mer == 0 && ser == 0)
   	{
   		for (int i = 0; i <= step; i++)
   		{
   			printf("(%d,%d)", mstep[i], sstep[i]);
   			if (i != step)
   				printf(" -> ");
   		}
   		printf("\n");
   		flag = true;
   	}
   ```

   （2）按运送方向分类讨论

   其中，变量before索引到此次运送之前的商人仆人的人数情况

   变量after索引到此次运送之后的商人仆人的人数情况

   变量before,after共同索引到无向图中的可行方案

   ```java
   for (int i = 0; i < 5; i++)
   	{
   		if (dir) {
   			int mnext = mer - cmer[i], snext = ser - cser[i];
   			if (mnext >= 0 && mnext < num + 1 && snext >= 0 && snext < num + 1 && state[mnext][snext])
   			{
   				int after = mnext * (num + 1) + snext;
   				if (!grid[before][after] && !grid[after][before])
   				{
   					grid[before][after] = 1;
   					grid[after][before] = 1;
   					DFS(mnext, snext, step + 1, !dir);
   					grid[before][after] = 0;
   					grid[before][after] = 0;
   				}
   			}
   		}
   		else {
   			int mnext = mer + cmer[i], snext = ser + cser[i];
   			if (mnext >= 0 && mnext < num + 1 && snext >= 0 && snext < num + 1 && state[mnext][snext])
   			{
   				int after = mnext * (num + 1) + snext;
   				if (!grid[before][after] && !grid[after][before])//满足条件并且未被访问过在无向图中建立一条边
   				{
   					grid[before][after] = 1;
   					grid[after][before] = 1;
   					DFS(mnext, snext, step + 1, !dir);
   					grid[before][after] = 0;
   					grid[before][after] = 0;
   				}
   			}
   		}
   	}
   ```

   

#### 代码

```java
#include"pch.h"
#include <cstdio>
#include<iostream>
#define maxn 100

using namespace std;
int num;
int grid[maxn*maxn][maxn*maxn];
int state[maxn][maxn];

int cmer[5] = { 2, 1, 0, 1, 0 };
int cser[5] = { 0, 1, 2, 0, 1 };
int mstep[maxn*maxn];
int sstep[maxn*maxn];


bool flag = false;
void DFS(int mer, int ser, int step, int dir)
{
	mstep[step] = mer, sstep[step] = ser;
	if (mer == 0 && ser == 0)
	{
		for (int i = 0; i <= step; i++)
		{
			printf("(%d,%d)", mstep[i], sstep[i]);
			if (i != step)
				printf(" -> ");
		}
		printf("\n");
		flag = true;
	}
	int before = mer * (num + 1) + ser;
	for (int i = 0; i < 5; i++)
	{
		if (dir) {
			int mnext = mer - cmer[i], snext = ser - cser[i];
			if (mnext >= 0 && mnext < num + 1 && snext >= 0 && snext < num + 1 && state[mnext][snext])
			{
				int after = mnext * (num + 1) + snext;
				if (!grid[before][after] && !grid[after][before])
				{
					grid[before][after] = 1;
					grid[after][before] = 1;
					DFS(mnext, snext, step + 1, !dir);
					grid[before][after] = 0;
					grid[before][after] = 0;
				}
			}
		}
		else {
			int mnext = mer + cmer[i], snext = ser + cser[i];
			if (mnext >= 0 && mnext < num + 1 && snext >= 0 && snext < num + 1 && state[mnext][snext])
			{
				int after = mnext * (num + 1) + snext;
				if (!grid[before][after] && !grid[after][before])
				{
					grid[before][after] = 1;
					grid[after][before] = 1;
					DFS(mnext, snext, step + 1, !dir);
					grid[before][after] = 0;
					grid[before][after] = 0;
				}
			}
		}
	}
}
int main()
{
	cin >> num;
	for (int i = 0; i < num + 1; i++)
	{
		state[i][0] = 1;
		state[i][num] = 1;
		state[i][i] = 1;
	}
	DFS(num, num, 0, 1);
	if (!flag)
		printf("they can't cross the river.");
}
```



## 优点和缺点

## 总结

