#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a,b=map(int,input().split())
if a+b>=15 and b>=8:
    print(1)
elif a+b>=10 and b>=3:
    print(2)
elif a+b>=3:
    print(3)
else:
    print(4)
