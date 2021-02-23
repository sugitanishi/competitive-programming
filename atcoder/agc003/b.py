import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=[int(input()) for i in range(n)]
ans=0
for i in range(len(a)):
    ans+=a[i]//2
    a[i]=a[i]%2
    if a[i]==1 and i+1<len(a) and a[i+1]>0:
        ans+=1
        a[i+1]-=1
print(ans)