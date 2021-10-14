#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
import typing
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

import random
import time
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
a=list(map(int,input().split()))

t=a[:]
for i in range(1,len(t)):
    t[i]+=t[i-1]

tt=t[:]
for i in range(1,len(tt)):
    tt[i]+=tt[i-1]

mx=0
for i in range(n):
    mx=max(a[i],mx)
    print(tt[i]+mx*(i+1))
