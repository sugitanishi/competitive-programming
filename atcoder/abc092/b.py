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
d,x=map(int,input().split())
a=[int(input()) for i in range(n)]
for i in range(n):
    j=1
    while (j)*a[i]+1<=d:
        j+=1
    x+=j
print(x)
