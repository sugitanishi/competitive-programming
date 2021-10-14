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

n,x=map(int,input().split())
h=list(map(int,input().split()))
g=[[]for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

used=set()
depth={}

def dfs(v,dp=0,p=-1):
    if v in used:
        return
    used.add(v)
    if dp in depth:
        depth[dp].append((v,p))
    else:
        depth[dp]=[(v,p)]
    for i in range(len(g[v])):
        tmp=dfs(g[v][i],dp+1,v)

dfs(x-1)
mx=max(depth.keys())
tmp=0
for i in reversed(range(1,mx+1)):
    for v,p in depth[i]:
        if h[v]>0:
            h[p]+=h[v]
            tmp+=1
print(2*tmp)