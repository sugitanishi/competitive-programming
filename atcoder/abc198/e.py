#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
c=list(map(int,input().split()))
g=[[] for i in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

que = deque()
que.append(0)
ans = []
memo=set([0])
used=[0 for i in range(10**5+1)]

def f(p):
    global ans
    if used[c[p]]==0:
        ans.append(p+1)
    used[c[p]]+=1
    for v in g[p]:
        if v not in memo:
            memo.add(v)
            f(v)
    used[c[p]]-=1
f(0)
print(*sorted(ans),sep='\n')
