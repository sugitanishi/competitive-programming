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

a,b,n=map(int,input().split())
a=[i for i in range(a,min(a+n,b+1))]
b=[i for i in range(max(a,b-n+1),b+1)]
print(*sorted(set(a)|set(b)))