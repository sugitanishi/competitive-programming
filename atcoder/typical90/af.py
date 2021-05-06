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
a=[list(map(int,input().split())) for i in range(n)]
m=int(input())
ng=[[False for i in range(n)] for i in range(n)]
for i in range(m):
    x,y=map(int,input().split())
    ng[x-1][y-1]=True
    ng[y-1][x-1]=True

mn=inf

for d in itertools.permutations(range(n)):
    tmp=0
    for i in range(n-1):
        if ng[d[i]][d[i+1]]:
            break
        tmp+=a[d[i]][i]
    else:
        mn=min(mn,tmp+a[d[-1]][n-1])
print(mn if mn!=inf else -1)

