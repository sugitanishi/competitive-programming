#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a,b,m=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
mn = min(al)+min(bl)
for i in range(m):
    x,y,c=map(int,input().split())
    mn = min(al[x-1]+bl[y-1]-c,mn)
print(mn)