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
t=list(map(int,input().split()))
m=int(input())
sm=sum(t)
for i in range(m):
    p,x=map(int,input().split())
    print(sm-t[p-1]+x)

