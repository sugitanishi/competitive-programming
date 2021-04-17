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

n,a,b=map(int,input().split())
ans=0
for i in range(1,n+1):
    sm = sum(map(int,str(i)))
    if a<=sm<=b:
        ans+=i
print(ans)