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

x=int(input())
mx=0
for i in range(1,x+1):
    for j in range(2,11):
        if i**j>x:
            break
        if i**j<=x:
            mx=max(mx,i**j)
print(mx)
