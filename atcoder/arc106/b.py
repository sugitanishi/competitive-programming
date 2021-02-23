import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

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

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
uf=UnionFind(n)
for i in range(m):
    c,d=map(int,input().split())
    uf.uni(c-1,d-1)

dic={}
for i in range(n):
    p=uf.root(i)
    if p not in dic:
        dic[p]=[0,0]
    dic[p][0]+=a[i]
    dic[p][1]+=b[i]
for k in dic:
    if dic[k][0]!=dic[k][1]:
        print('No')
        break
else:
    print('Yes')
