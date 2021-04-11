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

s=int(input())
def f(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1
used=set()
p=1
while True:
    if s in used:
        print(p)
        break
    used.add(s)
    s=f(s)
    p+=1