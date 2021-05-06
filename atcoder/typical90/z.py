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
que.append((0,1))
color=[-1 for i in range(n)]
while que:
    v,c=que.popleft()
    if color[v]>=0:
        continue
    color[v]=1-c
    for nxt in g[v]:
        if color[nxt]==-1:
            que.append((nxt,1-c))
ans_color=0 if color.count(0)>=n//2 else 1
ans=[]
for i in range(n):
    if color[i]==ans_color:
        ans.append(i+1)
print(*ans[:n//2])


