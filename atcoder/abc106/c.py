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

s=input()
k=int(input())
if '1' not in s:
    print(s[0])
else:
    if len(s)-len(s.lstrip('1'))>=k:
        print(1)
    else:
        print(s.lstrip('1')[0])
