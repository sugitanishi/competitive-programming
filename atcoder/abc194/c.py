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
a=list(map(int,input().split()))
b=[0 for i in range(n)]
ans=0
x=0
for i in range(n):
    ans+=a[i]*a[i]*(n-1)

b[n-1]=a[n-1]
for i in range(1,n):
    i=n-i-1
    b[i]=a[i]+b[i+1]

for i in range(n-1):
    x+=a[i]*b[i+1]
print(ans-2*x)



