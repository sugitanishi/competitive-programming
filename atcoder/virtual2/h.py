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

n,k=map(int,input().split())
t=[list(map(int,input().split())) for i in range(n)]
ans=0
for d in itertools.permutations(range(1,n)):
    d=[0]+list(d)+[0]
    tmp=0
    for i in range(len(d)-1):
        tmp += t[d[i]][d[i+1]]
    if tmp==k:
        ans+=1
print(ans)