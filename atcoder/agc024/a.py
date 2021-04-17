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

a,b,c,k=map(int,input().split())
if k%2==0:
    print(a-b)
else:
    print(b-a)
