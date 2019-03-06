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
