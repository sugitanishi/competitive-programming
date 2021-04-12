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

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
i=1
for p in itertools.permutations(range(1,n+1)):
    if list(p)==a:
        x=i
    if list(p)==b:
        y=i
    i+=1
print(abs(x-y))