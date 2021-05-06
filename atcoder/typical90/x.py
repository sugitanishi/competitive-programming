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

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sm=0
for i in range(n):
    sm+=abs(a[i]-b[i])

print('Yes' if k>=sm and (k-sm)%2==0 else 'No')