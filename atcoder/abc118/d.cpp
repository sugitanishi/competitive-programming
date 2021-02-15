#include <bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(n);i++)
using namespace std;
string ff(int n, int m, vector<int>&q,vector<int>&r, map<pair<int, int>, string>&memo) {
	if (memo.find(make_pair(n, m)) != memo.end()) {
		return memo[make_pair(n, m)];
	}
	if (n == 0) return "";
	string s = "";
	int f = 0;
	rep(i, m) {
		if (n - r[i] >= 0) {
			string tmp = ff(n - r[i], m, q, r, memo);
			if (tmp != "?") {
				tmp = to_string(q[i])+tmp;
				s = (s.size() != tmp.size()) ? ((s.size() > tmp.size()) ? s : tmp) : (s > tmp) ? s : tmp;
			}
			else {
				f++;
			}
		}
		else {
			f++;
		}
	}
	if (f == m) {
		return "?";
	}
	memo[make_pair(n, m)] = s;
	return s;
}
int main() {
	int n,m;
	cin >>n>>m;
	vector<int> a(m);
	rep(i, m)cin >> a[i];
	sort(a.begin(), a.end());

	vector<int> qq{ 1,2,3,4,5,6,7,8,9 };
	vector<int> rr{ 2,5,5,4,5,6,3,7,6 };
	vector<int> q;
	vector<int> r;
	for (int i = m - 1; i >= 0; i--) {
		q.push_back(qq[a[i] - 1]);
		r.push_back(rr[a[i] - 1]);
	}
	map<pair<int, int>, string> memo;
	cout << ff(n, m,q,r,memo) << endl;
	return 0;
}