import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
d=set()
for i in range(2,10**5+1):
    j=2
    while True:
        if i**j<=n:
            d.add(i**j)
        else:
            break
        j+=1
print(n-len(d))

