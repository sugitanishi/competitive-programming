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

n,m,x=map(int,input().split())
a=list(map(int,input().split()))
print(min(len(list(filter(lambda p:p>x,a))),len(list(filter(lambda p:p<x,a)))))
