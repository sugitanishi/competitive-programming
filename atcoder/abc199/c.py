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
s=list(input())
q=int(input())
rev=False

def f(a,b):
    if not rev:
        s[a],s[b]=s[b],s[a]
    else:
        a,b=(a+n)%(2*n),(b+n)%(2*n)
        s[a],s[b]=s[b],s[a]

for i in range(q):
    t,a,b=map(int,input().split())
    if t==1:
        f(a-1,b-1)
    else:
        rev=not rev

if not rev:
    print(''.join(s))
else:
    print(''.join(s[n:])+''.join(s[:n]))
