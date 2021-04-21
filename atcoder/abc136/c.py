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
a=list(map(int,input().split()))[::-1]
for i in range(1,n):
    if a[i]-a[i-1]>=2:
        print('No')
        break
    if a[i-1]<a[i]:
        a[i]-=1
else:
    print('Yes')
    