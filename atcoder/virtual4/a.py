#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache,reduce
from collections import deque
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
a=list(map(int,input().split()))
b=set(a)
if len(b)==1 and 0 in b:
    print('Yes')
elif len(b)==3:
    q,w,e=b
    if q^w^e==0 and a.count(q)==a.count(w)==a.count(e):
        print('Yes')
    else:
        print('No')
elif len(b)==2 and 0 in b:
    q,w=b
    if a.count(max(q,w))==a.count(0)*2:
        print('Yes')
    else:
        print('No')
else:
    print('No')