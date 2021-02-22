import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def divisors(n):
    d = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            d.append(i)
            if n//i != i:
                d.append(n//i)
        i += 1
    return sorted(d)

n=int(input())
ans=0
i=2
for i in divisors(n*2):
    if n*2//i!=n*2/i:
        continue
    else:
        if (n*2//i-(i-1))%2==0:
            ans+=1
print(ans)

