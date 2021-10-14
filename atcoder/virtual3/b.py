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
k=int(input())

count=0
while a>=b:
    b*=2
    count+=1
while b>=c:
    c*=2
    count+=1
print('Yes' if count<=k else 'No')