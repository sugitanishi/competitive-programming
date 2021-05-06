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
field=[[0 for i in range(1001)] for i in range(1001)]
for i in range(n):
    a,b,c,d=map(int,input().split())
    field[a][b]+=1
    field[a][d]-=1
    field[c][b]-=1
    field[c][d]+=1
for i in range(1001):
    for j in range(1001):
        if j!=0:
            field[i][j]+=field[i][j-1]

for j in range(1001):
    for i in range(1001):
        if i!=0:
            field[i][j]+=field[i-1][j]

ans=[0 for i in range(n+1)]
for i in range(1001):
    for j in range(1001):
        ans[field[i][j]]+=1
for i in range(1,n+1):
    print(ans[i])
