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
a=[input() for i in range(n)]
if len(set(a))!=n:
    print('No')
else:
    for i in range(1,n):
        if a[i-1][-1]!=a[i][0]:
            print('No')
            break
    else:
        print('Yes')