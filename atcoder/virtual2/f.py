#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

p=int(input())
def gcd(x,y):
    while x != 0:
        x,y=y%x,x
    return y
def lcm(x,y):
    return (x * y)//gcd(x, y)

ans=0
for i in range(1,p+1):
    for j in range(1,p+1):
        for k in range(1,p+1):
            ans+=gcd(i,gcd(j,k))
print(ans)