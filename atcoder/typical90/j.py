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
a=[[0] for i in range(2)]
for i in range(n):
    c,p=map(int,input().split())
    c-=1
    a[c].append(a[c][-1]+p)
    a[1-c].append(a[1-c][-1])

q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(a[0][r]-a[0][l-1],a[1][r]-a[1][l-1])
