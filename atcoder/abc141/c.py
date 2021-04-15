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

n,k,q=map(int,input().split())
a=[0 for i in range(n+2)]
for i in range(q):
    p=int(input())
    a[0]-=1
    a[p]+=1
    a[p+1]-=1
    a[-1]+=1
a=list(itertools.accumulate(a))
for i in range(n):
    a[i+1]+=k
    if a[i+1]>0:
        print('Yes')
    else:
        print('No')
