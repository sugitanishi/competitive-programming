import sys
sys.setrecursionlimit(100000)
class UnionFind:
    def __init__(self, n):
        self.p=[i for i in range(n)]
        self.r=[0 for i in range(n)]
    
    def root(self,x):
        if self.p[x]==x:
            return x
        else:
            self.p[x] = self.root(self.p[x])
            return self.p[x]
    
    def uni(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if(x==y):
            return
        if self.r[x]<self.r[y]:
            self.p[x]=y
        else:
            self.p[y]=x
            if self.r[x]==self.r[y]:
                self.r[x]+=1
    
    def same(self,x,y):
        return self.root(x)==self.root(y)

n,m=map(int,input().split())
p=list(map(int,input().split()))
uf=UnionFind(n)
for i in range(m):
    x,y=map(int,input().split())
    uf.uni(p[x-1]-1,p[y-1]-1)
count=0
for i in range(n):
    if uf.same(i,p[i]-1):
        count+=1
print(count)