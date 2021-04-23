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

n,l=map(int,input().split())
k=int(input())
a=[0]+list(map(int,input().split()))+[l]

def ok(s):
    count=0
    tmp=0
    for i in range(1,len(a)):
        tmp+=a[i]-a[i-1]
        if tmp>=s:
            tmp=0
            count+=1
    return count>=k+1

l,r=1,10**9+1
while l+1<r:
    mid=(l+r)//2
    if ok(mid):
        l=mid
    else:
        r=mid
print(l)