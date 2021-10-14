#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache, reduce
from collections import deque
import heapq
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
a=set(map(int,input().split()))
def gcd(x,y):
    while x != 0:
        x,y=y%x,x
    return y
def lcm(x,y):
    return (x * y)//gcd(x, y)
print(reduce(gcd,a))