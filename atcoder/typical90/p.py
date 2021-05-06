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
a,b,c=map(int,input().split())

mn=inf
for i in range(10000):
    for j in range(10000-i):
        if n-(i*a+j*b)<0:
            break
        if (n-(i*a+j*b))%c==0:
            mn=min(mn,i+j+(n-(i*a+j*b))//c)
print(mn)

