import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

class TravelingSalesmanSolver:
    # n頂点 頂点0からすべてを通って頂点0に戻るコストの最小を求める
    # O(n^2 2^n)
    def __init__(self, n, nodes=None, dist_func=None, dist_matrix=None, inf=10**18):
        self.size=n
        self.inf=inf
        self.dp=[[self.inf for _ in range(n)] for _ in range(2**n)]
        # 頂点情報と2頂点間のコストを与える場合
        self.nodes=nodes
        self.dist_func=dist_func
        # 前計算された頂点間コストのマトリクスを与える場合
        self.dist_matrix=dist_matrix
    
    def solve(self):
        if self.dist_matrix is None:
            self.dist_matrix=[[self.inf for _ in range(self.size)] for _ in range(self.size)]
            for i in range(self.size):
                for j in range(self.size):
                    self.dist_matrix[i][j]=self.dist_func(self.nodes[i],self.nodes[j])
        return self._solve()

    def _solve(self):
        self.dp[0][0]=0
        for S in range(2**self.size):
            for v in range(self.size):
                for u in range(self.size):
                    if S!=0 and not (S&(1<<u)):
                        continue
                    if S&(1<<v)==0 and v!=u:
                        self.dp[S|(1 << v)][v] = min(
                            self.dp[S|(1 << v)][v],
                            self.dp[S][u]+self.dist_matrix[u][v]
                        )
        return self.dp[2**self.size-1][0]

n=int(input())
d=[tuple(map(int,input().split())) for i in range(n)]
tss=TravelingSalesmanSolver(n,d,lambda a,b:abs(a[0]-b[0])+abs(a[1]-b[1])+max(0,b[2]-a[2]))
print(tss.solve())
