#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

c,x,y=map(int,input().split())

def ok(p):
    return (c*p)**2>=x*x+y*y

l,r=0,400000000
while l+1<r:
    mid=(l+r)//2
    if ok(mid):
        r=mid
    else:
        l=mid
if r==1 and (c*r)**2>x*x+y*y:
    print(2)
else:
    print(r)