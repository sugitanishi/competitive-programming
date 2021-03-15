#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n=int(input())
print(max(n-999,0)+max(n-999999,0)+ \
max(n-999999999,0)+max(n-999999999999,0)+ \
max(n-999999999999999,0)+max(n-999999999999999999,0))

