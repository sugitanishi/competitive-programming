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
c=[]
for i in range(n):
    c.append(list(map(int,input().split())))
a,b=[0 for i in range(n)],[0 for i in range(n)]
for i in range(1,n):
    b[i]=b[i-1]+c[0][i]-c[0][i-1]
mn=min(b)
b=[b[i]-mn for i in range(n)]
a=[c[i][0]-b[0] for i in range(n)]

for i in range(n):
    for j in range(n):
        if c[i][j]!=a[i]+b[j]:
            print('No')
            exit()
print('Yes')
print(*a)
print(*b)
