#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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

def field_id(y,x):
    return w*y+x

h,w=map(int,input().split())
field=[[0 for i in range(w)] for i in range(h)]
uf=UnionFind(h*w)
dx=[1,0,-1,0]
dy=[0,1,0,-1]

q=int(input())
for i in range(q):
    in_data=list(map(int,input().split()))
    query=in_data[0]
    if query==1:
        y,x=in_data[1:]
        field[y-1][x-1]=1
        for j in range(4): 
            if 0<=y-1+dy[j]<h and 0<=x-1+dx[j]<w and field[y-1+dy[j]][x-1+dx[j]]==1:
                uf.uni(field_id(y-1,x-1),field_id(y-1+dy[j],x-1+dx[j]))
    else:
        a,b,c,d=in_data[1:]
        print('Yes' if uf.same(field_id(a-1,b-1),field_id(c-1,d-1)) and field[a-1][b-1]==field[c-1][d-1]==1 else 'No')
