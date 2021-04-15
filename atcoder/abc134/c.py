#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
a=[int(input()) for i in range(n)]

mx=max(a)
sa=set(a)
if a.count(mx)>=2:
    print(*[mx]*n,sep='\n')
else:
    sa.remove(mx)
    mx_2=max(sa)
    for i in range(n):
        if a[i]==mx:
            print(mx_2)
        else:
            print(mx)

