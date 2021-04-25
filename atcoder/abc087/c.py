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
a=[list(map(int,input().split())),list(map(int,input().split()))]
mx=0
for i in range(n):
    count=0
    for j in range(i+1):
        count+=a[0][j]
    for k in range(i,n):
        count+=a[1][k]
    mx=max(mx,count)
print(mx)


