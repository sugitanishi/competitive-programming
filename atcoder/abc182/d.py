import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=[0]+list(map(int,input().split()))
a_acm=list(itertools.accumulate(a))
a_max=[0]
for i in range(1,n+1):
    a_max.append(max(a_max[-1],a_acm[i]))

ans=0
p=0
for i in range(1,n+1):
    ans=max(p+a_acm[i],p+a_max[i],ans)
    p+=a_acm[i]
print(ans)

