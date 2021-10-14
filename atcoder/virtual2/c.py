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
ans=[0 for i in range(n+1)]
for i in range(1,101):
    for j in range(1,n-i**2+1):
        for k in range(1,n-i**2-j**2-i*j+1):
            tmp=i**2+j**2+k**2+i*j+j*k+k*i
            if n<tmp:
                break
            ans[tmp]+=1

print(*ans[1:],sep='\n')