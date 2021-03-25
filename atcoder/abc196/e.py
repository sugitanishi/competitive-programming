#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
import bisect
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
mn=[]
mx=[]
sm=0
for i in range(n):
    a,t=map(int,input().split())
    if t==2:
        mn.append(a)
    elif t==3:
        mx.append(a)
    sm+=a
mn=sorted(mn)
mna=[0]+list(itertools.accumulate(mn))
mx=sorted(mx)
mxa=[0]+list(itertools.accumulate(mx))
q=int(input())
d=list(map(int,input().split()))
for x in d:
    print(x,sm,mn,mx)
    y=bisect.bisect_left(mn,x)
    z=bisect.bisect_left(mx,x)
    ans=x+sm-x*(len(mn)-y)-mna[y]-x*z-(mxa[-1]-mxa[z])
    print(ans)