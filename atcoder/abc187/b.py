#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
import cmath
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
d=[]
ans=0
for i in range(n):
    d.append(complex(*list(map(int,input().split()))))
for i in range(n):
    for j in range(i+1,n):
        x=d[j]-d[i]
        y=d[i]-d[j]
        if cmath.phase(complex(1,-1))<=cmath.phase(x)<=cmath.phase(complex(1,1)):
            ans+=1
        elif cmath.phase(complex(1,-1))<=cmath.phase(y)<=cmath.phase(complex(1,1)):
            ans+=1
print(ans)
