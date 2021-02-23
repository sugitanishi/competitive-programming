import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
a=list(map(int,input().split()))
s={1}
d=[1]
p=0
while True:
    if a[p] not in s:
        s.add(a[p])
        d.append(a[p])
        p=a[p]-1
    else:
        q,w=d[:d.index(a[p])],d[d.index(a[p]):]
        break
if k<len(d):
    print(d[k])
else:
    print(w[(k-len(q)+1)%len(w)-1])
