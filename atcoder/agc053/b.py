#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
from heapq import heappush, heappop, heapify
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
v=list(map(int,input().split()))
sm=sum(v)
used=set()
que = []
for i in range(n):
    heappush(que,v[n-i-1])
    heappush(que,v[n+i])
    t=heappop(que)
    sm-=t
print(sm)
