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

def divisors(n):
    d = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if n//i != i:
                d.append(n//i)
        i += 1
    return sorted(d)

n=int(input())
div=divisors(n)
point=[]
for i in range(ceil(len(div)/2)):
    point.append((div[i],div[-(i+1)]))

mn=inf
for x,y in point:
    mn=min(mn,x-1+y-1)
print(mn)
