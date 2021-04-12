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

n,m=map(int,input().split())
l_max=1
r_min=10**5
for i in range(m):
    l,r=map(int,input().split())
    l_max=max(l_max,l)
    r_min=min(r_min,r)
print(max(r_min-l_max+1,0))
