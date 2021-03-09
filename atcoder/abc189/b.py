#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n,limit=map(int,input().split())
now=0
for i in range(n):
    a,b=map(int,input().split())
    now += a*b
    if now/100>limit:
        print(i+1)
        break
else:
    print(-1)


