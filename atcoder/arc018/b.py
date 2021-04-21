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

def is_line(x1,y1,x2,y2,x3,y3):
    return (x1-x2)*(y1-y3)==(x1-x3)*(y1-y2)

n=int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append((x,y))

ans=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            x1,y1=a[i]
            x2,y2=a[j]
            x3,y3=a[k]
            if is_line(x1,y1,x2,y2,x3,y3):
                continue
            if ((abs(x1-x2)*abs(y1-y2))%2 +
                (abs(x3-x2)*abs(y3-y2))%2 +
                (abs(x1-x3)*abs(y1-y3))%2)%2 == 0:
                ans+=1
print(ans)