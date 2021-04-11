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

def bingo():
    for i in range(3):
        if sum(a[i])==0:
            return True
    for j in range(3):
        if sum([a[k][j] for k in range(3)])==0:
            return True
    if sum([a[i][i] for i in range(3)])==0:
        return True
    if sum([a[i][2-i] for i in range(3)])==0:
        return True
    return False

a=[list(map(int,input().split())) for i in range(3)]
n=int(input())
for i in range(n):
    t=int(input())
    for j in range(3):
        for k in range(3):
            if a[j][k]==t:
                a[j][k]=0
print('Yes' if bingo() else 'No')

