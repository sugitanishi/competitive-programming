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
    a,b,c=map(int,input().split())
    g[a-1].append((c,b-1))
    g[b-1].append((c,a-1))

def dijkstra(g,st):
    from heapq import heappush, heappop, heapify
    inf=10**18
    dist=[inf for i in range(len(g))]
    visited=[False for i in range(len(g))]
    dist[st]=0
    que=[]
    heappush(que,(0,st))
    while que:
        c,v=heappop(que)
        if visited[v]:
            continue
        visited[v]=True
        for x in g[v]:
            tmp=x[0]+c
            if tmp<dist[x[1]] and not visited[x[1]]:
                dist[x[1]]=tmp
                heappush(que,(tmp,x[1]))
    return dist

d0=dijkstra(g,0)
dn=dijkstra(g,n-1)

for i in range(n):
    print(d0[i]+dn[i])
