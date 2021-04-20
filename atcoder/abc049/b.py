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

h,w=map(int,input().split())
c=[input() for i in range(h)]
field=[[c[i//2][j] for j in range(w)]for i in range(h*2)]

for i in range(h*2):
    print(*field[i],sep='')