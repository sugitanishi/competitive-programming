#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n,x=map(int,input().split())
a=sorted(list(map(int,input().split())))
ans=0
for i in range(n):
    if x>=a[i]:
        x-=a[i]
        ans+=1
    else:
        break
else:
    if x!=0:
        ans=max(ans-1,0)
print(ans)
