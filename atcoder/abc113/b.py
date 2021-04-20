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
t,a=map(int,input().split())
h=list(map(int,input().split()))
mn=sorted(h,key=lambda x:abs(a*1000-(t*1000-x*6)))[0]
for i in range(n):
    if h[i]==mn:
        print(i+1)