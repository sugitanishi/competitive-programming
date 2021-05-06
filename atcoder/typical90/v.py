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

a,b,c=map(int,input().split())

def gcd(x,y):
    while x != 0:
        x,y=y%x,x
    return y
def lcm(x,y):
    return (x * y)//gcd(x, y)

p=gcd(gcd(a,b),c)
print(a//p-1+b//p-1+c//p-1)