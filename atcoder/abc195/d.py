#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n,m,q=map(int,input().split())
item=[]
for i in range(n):
    item.append(tuple(map(int,input().split())))
item=sorted(item, key=lambda x:(-x[1],-x[0]))
x=list(map(int,input().split()))

for _ in range(q):
    ans=0
    a,b=map(int,input().split())
    ub=sorted(x[:a-1]+x[b:])
    used=[False for i in range(n)]
    for i in range(len(ub)):
        for j in range(n):
            if item[j][0]<=ub[i] and not used[j]:
                ans+=item[j][1]
                used[j]=True
                break
    print(ans)

