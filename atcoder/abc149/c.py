#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def is_prime(n):
    n = abs(n)
    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False
    d = n-1
    while d & 1 == 0:
        d >>= 1
    seed_primes = [2,7,61] if n < 4294967296 else [2,3,5,7,11,13,17,19,23,29,31,37]
    for a in seed_primes:
        if a >= n:
            continue
        t = d
        y = pow(a,t,n)
        while t != n-1 and y != 1 and y != n-1:
            y = (y * y) % n
            t <<= 1
        if y != n-1 and t & 1 == 0:
            return False
    return True

x=int(input())
while not is_prime(x):
    x+=1
print(x)
