import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
b=list(map(int,input().split()))

memo={}
def solve(a):
    if a in memo:
        return memo[a]
    if len(a)==0:
        return []
    for i in range(len(a)):
        i=len(a)-i-1
        if a[i]==i+1 and i+1<=len(a):
            ret = solve(a[:i]+a[i+1:])
            if ret != None:
                memo[a]=ret+[i+1]
                return memo[a]
            return None
    memo[a]=None
    return None

ans=solve(tuple(b))
if ans==None:
    ans=[-1]
print(*ans,sep='\n')

