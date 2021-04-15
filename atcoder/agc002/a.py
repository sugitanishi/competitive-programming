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

a,b=map(int,input().split())
if a<=0 and b>=0:
    print('Zero')
elif a>0 and b>0:
    print('Positive')
elif (b-a)%2!=0:
    print('Positive')
else:
    print('Negative')