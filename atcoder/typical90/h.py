#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
inf=10**20
mod=10**9+7
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
s="$"+input()
atcoder="$atcoder"

memo={}
def f(p,q):
    if (p,q) in memo:
        return memo[(p,q)]
    if p<q:
        return 0
    if q==0:
        return 1
    ret = f(p-1,q)
    if s[p]==atcoder[q]:
        ret+=f(p-1,q-1)
    memo[(p,q)]=ret%mod
    return memo[(p,q)]

print(f(n,7))
