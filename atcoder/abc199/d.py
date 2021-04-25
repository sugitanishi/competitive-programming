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

    def uni(self,xx,yy):
        x=self.root(xx)
        y=self.root(yy)
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
uf=UnionFind(n)
g=[[]for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    uf.uni(a-1,b-1)

group={i:[i] for i in range(n) if uf.data[i]<0}

for i in range(n):
    if uf.data[i]>=0:
        group[uf.root(i)].append(i)

def order(g,gr,gr_f,v):
    ordlist=[]
    used=[False for i in range(len(gr))]
    que=deque()
    que.append(v)
    while que:
        x=que.popleft()
        if used[x]:
            continue
        used[x]=True
        ordlist.append(x)
        for nxt in g[gr[x]]:
            nxt=gr_f[nxt]
            if not used[nxt]:
                que.append(nxt)
    return ordlist


ans=1
for gr in group.values():
    que=deque()
    tmp=[-1 for i in range(len(gr))]
    tmp[0]=0
    que.append((tmp,1))
    gr_ans=0
    gr_f={gr[i]:i for i in range(len(gr))}
    ordlist=order(g,gr,gr_f,0)
    assert(len(set(ordlist)-set(range(len(gr))))==0)
    while que:
        arr,k=que.popleft()
        if k==len(gr):
            gr_ans+=1
            continue
        s={0,1,2}
        for j in range(len(g[gr[ordlist[k]]])):
            w=arr[gr_f[g[gr[ordlist[k]]][j]]]
            if w in s:
                s.remove(w)
            if len(s)==0:
                break
        for p in s:
            if k+1==len(gr):
                gr_ans+=1
            else:
                arr_r=arr[:]
                arr_r[ordlist[k]]=p
                que.append((arr_r,k+1))
    ans*=gr_ans*3
print(ans)
