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
field=[list(map(int,input().split())) for i in range(h)]
ho=[0 for i in range(h)]
va=[0 for i in range(w)]

for i in range(h):
    for j in range(w):
        ho[i]+=field[i][j]
        va[j]+=field[i][j]

for i in range(h):
    for j in range(w):
        field[i][j]=ho[i]+va[j]-field[i][j]
    print(*field[i])

