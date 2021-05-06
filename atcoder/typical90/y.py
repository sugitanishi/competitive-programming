#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache,reduce
from collections import deque,Counter
from operator import mul
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a,b=map(int,input().split())

def ok(x,y):
    return Counter(x)==Counter(y)

ans=0
for j in range(1,len(str(a))+1):
    for d in itertools.combinations_with_replacement(range(10), j):
        fx=reduce(mul, d)
        if fx+b<=a and ok(d,map(int,str(fx+b))):
            ans+=1
print(ans)