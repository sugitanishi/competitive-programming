import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,m=map(int,input().split())
class UnionFind:
    def __init__(self, n):
        self.data=[-1 for i in range(n)]

    def root(self,x):
        if self.data[x]<0:
            return x
        else:
            self.data[x]=self.root(self.data[x])
            return self.data[x]

    def uni(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if(x==y):
            return
        if self.data[y]<self.data[x]:
            x,y=y,x
        self.data[x]+= self.data[y]
        self.data[y] = x

    def same(self,x,y):
        return self.root(x)==self.root(y)

    def size(self,x):
        return -self.data[self.root(x)]
uf=UnionFind(n)
for i in range(m):
    a,b=map(int,input().split())
    uf.uni(a-1,b-1)
print(-min(uf.data))