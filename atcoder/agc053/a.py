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
s=input()
a=list(map(int,input().split()))

def good(a):
    if min(a)<0:
        return False
    for i in range(n):
        if s[i]=='<' and a[i]>=a[i+1]:
            return False
        if s[i]=='>' and a[i]<=a[i+1]:
            return False
    return True

def mnn(a):
    mn=999999999999
    for i in range(n):
        mn=min(abs(a[i]-a[i+1]),mn)
    return mn

ans=[]
while True:
    mn = mnn(a)
    tmp = [a[i]//mn for i in range(n+1)]
    if good([a[i]-tmp[i] for i in range(n+1)]):
        ans.append(tmp)
        a=[a[i]-tmp[i] for i in range(n+1)]
    else:
        ans.append(a[:])
        break

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

