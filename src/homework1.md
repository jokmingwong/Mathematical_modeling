# 第一次作业

## 摘要

## 背景

## 模型假设

  (扯一下仆人下不下船的临界条件)



提出假设：（以商人数是3人为例）

1. 商人和仆人从北岸出发，目的地是南岸

2. `mer`表示某次运送前北岸商人的人数，`ser`表示某次运送前仆人的人数，

3. `mnext`和`snext`分别表示某次运送后北岸商人的数量，北岸仆人的数量

   则运送过程中需要满足以下的条件

   （1）$ mer \in [0,3]$

   （2）$ser \in [0,3]​$

   （3）$state[mer][ser]$ 

## 模型建立

### 模型：回溯分析

回溯模型即使用暴力的解法，一个状态接着一个状态的遍历，若当前状态不符合商人存活的条件，则回溯到上一个能使商人存活的状态。

每个状态Status有两个值即$x$(商人数量)和$y$(随从数量)。

每次状态变化之后都有:

1. 在河的南岸要保证商人存活且不存在有负数个人数的情况，公式如下

   $CurrentStatus.x \ge 0 \and CurrentStatus.y \ge0\and CurrentStatus.x\ge CurrentStatus.y​$

2. 同时在河的北岸也要保证商人存活且不存在负数个人数的情况，公式如下

   $CurrentStatus.x \ge 0 \and CurrentStatus.y \ge0 \and N-CurrentStatus.x \ge N-CurrentStatus.y  $

3. 每次一个方向上有五种变化选择,为向对面方向输送$(x,y)$个人:

   $(0,1),(1,0),(2,0),(1,1),(0,2)$



利用了C++中完善的STL库实现了这个模拟。

```cpp
#include<cstdio>
#include<vector>
#include<unordered_set>
using namespace std;
struct Status {
	int x, y;
	Status operator+(const Status s) {
		return { x + s.x,y + s.y };
	}
	Status operator-(const Status s) {
		return { x - s.x,y - s.y };
	}
	Status(const int _x, const int _y):x(_x), y(_y){};
};


class PathStack {
public:
	PathStack() {
		ll.clear();
	}
	void push(Status s) {
		ll.push_back(s);
	}
	void pop() {
		ll.pop_back();
	}
	void showPath() {
		for (Status s : ll) {
			printf("(%d,%d)\n");
		}
	}
private:
	vector<Status>ll;
};
// record the direction
const static Status MoveNorth[5] = { {-1,0},{-1,-1},{-2,0},{0,-1},{0,-2} };
const static Status MoveSouth[5] = { {1,0},{1,1},{2,0},{0,1},{0,2} };
// record the correct path
PathStack path;
// record the status and construct a hash function
bool operator==(const Status& s1, const Status& s2) {
	return s1.x == s2.x&&s1.y == s2.y;
}
struct StatusHash {
	size_t operator()(const Status& _s)const {
		return hash<int>()(10 * _s.x + _s.y);
	}
};
unordered_set<Status,StatusHash>status_mark;


// the number of the bussinessman and the servant
int N;
bool PathIsFound = false;
void CrossRiver(Status cur,bool isMovingNorth) {
	if (cur.x == 0 && cur.y == 0) {
		PathIsFound = true;
		printf("Found it and the move status are below:\n");
		path.showPath();
		system("pause");
	}
	// it meet the demand and never happen before
	if (status_mark.find(cur) == status_mark.end()&&cur.x>=cur.y&&N-cur.x>=N-cur.y&&cur.x>=0&&cur.y>=0&&cur.x) {
		status_mark.insert(cur);
		path.push(cur);
		if (isMovingNorth) {
			int i;
			for (i = 0; i < 5; i++) {
				CrossRiver(cur + MoveNorth[i], !isMovingNorth);
			}
			if (!PathIsFound)path.pop();
		}
		else {
			int i;
			for (i = 0; i < 5; i++) {
				CrossRiver(cur + MoveSouth[i], isMovingNorth);
			}
			if (!PathIsFound)path.pop();

		}
	}
}

int main() {
	printf("Input the number of bussinessmans and the servants:\n");
	scanf("%d", &N);
	path = *(new PathStack());
	Status current = { N,N };
	CrossRiver(current, true);
	printf("Not found!\n");
	return 0;
}
```









### 模型：无向图结构模型

使用二维向量state 和 grid 的数据结构（以商人数量3为例）

| 仆人 \| 商人 | 0    | 1    | 2    | 3    |
| ------------ | ---- | ---- | ---- | ---- |
| 0            | 1    | 0    | 0    | 1    |
| 1            | 1    | 1    | 0    | 1    |
| 2            | 1    | 0    | 1    | 1    |
| 3            | 1    | 0    | 0    | 1    |

​										表1：二维向量state

布尔值二维向量state，描述北岸（出发岸）商人和仆人人数的可行解，如：商人1人，仆人1人，可行表示为1；如：商人2人，仆人1人，则对岸商人1人，仆人两人，不满足条件。

| 0    | 0    | 0    | 0    |
| ---- | ---- | ---- | ---- |
| 0    | 0    | 0    | 0    |
| 0    | 0    | 0    | 0    |
| 0    | 0    | 0    | 0    |

​                                                                               表2：二维向量grid

布尔值二维向量grid，描述北岸（出发岸）人数与运走人数之间的可行关系，即无向图结构的邻接矩阵，如向量值`grid[before][after] == grid[after][before] == 1`,则证明已访问过图中该点。

#### 代码

```cpp
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

