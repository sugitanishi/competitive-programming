import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if sum(a)<sum(b):
    print(-1)
    exit()
plus=[]
minus=[]
for i in range(n):
    if a[i]>b[i]:
        plus.append(a[i]-b[i])
    elif b[i]>a[i]:
        minus.append(b[i]-a[i])
plus=sorted(plus)[::-1]
minus_sum=sum(minus)
tmp=0
for i in range(n):
    if tmp>=minus_sum:
        print(i+len(minus))
        break
    tmp+=plus[i]


