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
b=list(map(int,input().split()))
a=[inf for i in range(n)]
for i in range(1,n):
    if a[i-1]>b[i-1]:
        a[i-1]=b[i-1]
    if a[i]>b[i-1]:
        a[i]=b[i-1]
print(sum(a))