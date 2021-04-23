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
ans=[]
for x in range(2**n):
    count=0
    ok=True
    for i in range(n):
        if x&(1<<i):
            count+=1
        else:
            count-=1
        if count<0:
            ok=False
    if count>0:
        ok=False
    if ok:
        tmp=[]
        for i in range(n):
            if x&(1<<i):
                tmp.append('(')
            else:
                tmp.append(')')
        ans.append(''.join(tmp))
print(*sorted(ans),sep='\n')

