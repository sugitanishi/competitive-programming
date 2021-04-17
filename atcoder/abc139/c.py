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

mx=0
count=0
n=int(input())
h=list(map(int,input().split()))
for i in range(1,n):
    if h[i-1]>=h[i]:
        count+=1
        mx=max(mx,count)
    else:
        count=0
print(mx)