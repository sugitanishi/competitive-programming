#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import cmath
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
d=[]
for i in range(n):
    d.append(tuple(map(int,input().split())))
d=sorted(d)
d=list(map(lambda x:complex(*x),d))

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if cmath.phase(d[j]-d[i]) == cmath.phase(d[k]-d[j]):
                print('Yes')
                exit()
print('No')