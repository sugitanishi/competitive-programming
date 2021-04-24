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

n,m=map(int,input().split())

g=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

# gは有向グラフの隣接リスト表現
def scc(g,rg=None):
    rg=[[] for i in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g[i])):
            rg[g[i][j]].append(i)
    used=[False for i in range(len(g))]
    vs=[]
    group=[]
    def dfs(v):
        used[v]=True
        for nxt in g[v]:
            if not used[nxt]:
                dfs(nxt)
        vs.append(v)
    
    def rdfs(v,k):
        used[v]=True
        if len(group)<=k:
            group.append([])
        group[k].append(v)
        for nxt in rg[v]:
            if not used[nxt]:
                rdfs(nxt,k)
    
    for i in range(len(g)):
        if not used[i]:
            dfs(i)
    used=[False for i in range(len(g))]
    k=0
    for i in range(len(vs)):
        i=len(vs)-i-1
        if not used[vs[i]]:
            rdfs(vs[i],k)
            k+=1
    return group,k # 強連結成分グループ, その個数

group,_k=scc(g)

ans=0
for i in range(len(group)):
    ans+=len(group[i])*(len(group[i])-1)//2
print(ans)