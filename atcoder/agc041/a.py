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

n,a,b=map(int,input().split())
if (b-a)%2==0:
    print((b-a)//2)
else:
    print(min(a+(b-a-1)//2,(n-b+1)+(n-(a+(n-b+1)))//2))