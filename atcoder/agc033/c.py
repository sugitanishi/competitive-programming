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

n=int(input())
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

used=[False]*n

def dfs(v,d=0):
    used[v]=True
    x,y=-1,-1
    for i in range(len(g[v])):
        if used[g[v][i]]:
            continue
        tx,ty=dfs(g[v][i],d+1)
        if y<ty:
            x=tx
            y=ty
    if (x,y)==(-1,-1):
        return v,d
    return x,y

p,q=dfs(0)
used=[False]*n
p,q=dfs(p)
print('First' if q%3!=1 else 'Second')
