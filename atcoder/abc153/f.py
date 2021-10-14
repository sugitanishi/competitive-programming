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

n,d,a=map(int,input().split())
en=[]
for i in range(n):
    x,h=map(int,input().split())
    en.append((x,h))
en=sorted(en)
mk=[]
p=0

for i in range(n):
    while p+1<n and en[p+1][0]-en[i][0]<=2*d: p+=1
    mk.append(p)

ac=[0 for i in range(n+1)]
ans=0
for i in range(n):
    if i!=0:
        ac[i]+=ac[i-1]
    tmp=ceil(max((en[i][1]-ac[i]*a),0)/a)
    ac[i]+=tmp
    ans+=tmp
    ac[mk[i]+1]-=tmp
print(ans)

