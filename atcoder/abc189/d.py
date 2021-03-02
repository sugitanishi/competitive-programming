#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
d=[input() for i in range(n)]

@lru_cache(maxsize=1000000)
def solve(x,f):
    if x==0:
        return 1
    if f:
        if d[x-1]=='OR':
            return 2*solve(x-1,True)+solve(x-1,False)
        else:
            return solve(x-1,True)
    else:
        if d[x-1]=='OR':
            return solve(x-1,False)
        else:
            return solve(x-1,True)+2*solve(x-1,False)

print(solve(n,True))

