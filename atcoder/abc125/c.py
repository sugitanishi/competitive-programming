#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

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

def check(x):
    ng=0
    for i in range(n):
        if a[i]%x!=0:
            ng+=1
    return ng

s=set()
n=int(input())
a=list(map(int,input().split()))

mx=0
for i in range(2):
    for x in divisors(a[i]):
        if mx<x and check(x)<=1:
            mx=x
print(mx)