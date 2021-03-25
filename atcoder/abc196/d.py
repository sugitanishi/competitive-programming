#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache, reduce
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

h,w,a,b=map(int,input().split())
d=[[] for i in range(h*w)]
count=0
for i in range(h):
    for j in range(w):
        if j+1<w:
            d[count].append(count+1)
        if j-1>=0:
            d[count].append(count-1)
        if i-1>=0:
            d[count].append(count-w)
        if i+1<h:
            d[count].append(count+w)
        count+=1

memo=set()
def solve(used,field,x):
    if (field,x) in memo:
        return 0
    memo.add((field,x))
    if x==0:
        return 1
    ans=0
    for i in range(h*w):
        for j in range(i+1,h*w):
            if j in d[i] and (i not in used) and (j not in used):
                ans += solve(used|frozenset((i,j)),field|frozenset(((i,j),)),x-1)
    return ans

print(solve(frozenset(),frozenset(),a))
