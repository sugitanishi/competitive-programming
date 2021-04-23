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

que=deque()
que.append(0)
used=[False for i in range(n)]
left=-1
while que:
    v=que.popleft()
    left=v
    used[v]=True
    for nxt in g[v]:
        if not used[nxt]:
            que.append(nxt)

que=deque()
que.append((left,0))
used=[False for i in range(n)]
mx=0
while que:
    v,c=que.popleft()
    used[v]=True
    mx=c
    for nxt in g[v]:
        if not used[nxt]:
            que.append((nxt,c+1))
print(mx+1)