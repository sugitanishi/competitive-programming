#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
a=[]
b=[]
for i in range(n):
    aa,bb=map(int,input().split())
    a.append(aa)
    b.append(bb)

mn=999999999999999999999
for i in range(n):
    for j in range(n):
        if i==j:
            mn=min(mn,a[i]+b[j])
        else:
            mn=min(mn,max(a[i],b[j]))

print(mn)


