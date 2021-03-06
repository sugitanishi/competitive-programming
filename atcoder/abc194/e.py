#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n,m=map(int,input().split())
a=list(map(int,input().split()))
d=[0 for i in range(1500001)]
for i in range(m):
    d[a[i]]+=1

ans=9999999999999999
for i in range(1500001):
    if d[i]==0:
        ans=i
        break

for i in range(1,n-m+1):
    d[a[i-1]]-=1
    d[a[i+m-1]]+=1
    if d[a[i-1]]==0:
        ans=min(ans,a[i-1])

print(ans)