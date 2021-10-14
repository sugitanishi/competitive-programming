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

s,p=map(int,input().split())
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
dv=divisors(p)
for x in dv:
    if s-x==p//x:
        print('Yes')
        break
else:
    print('No')