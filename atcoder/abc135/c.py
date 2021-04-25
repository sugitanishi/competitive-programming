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
a=list(map(int,input().split()))
x=list(map(int,input().split()))
sm=sum(a)
for i in range(n):
    b,a[i]=max(x[i]-a[i],0),max(a[i]-x[i],0)
    a[i+1]=max(a[i+1]-b,0)
print(sm-sum(a))
