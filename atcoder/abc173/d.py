import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=sorted(list(map(int,input().split())))[::-1]

ans=0
p=0
for i in range(1,n):
    ans+=a[p]
    if i%2==1:
        p+=1
print(ans)
