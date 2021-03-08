#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache, reduce
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def comb(a,b):
    numerator = reduce(lambda a,b:a*b,range(a-b+1,a+1))
    denominator = reduce(lambda a,b:a*b,range(1,b+1))
    return numerator//denominator

m=int(input())
print(comb(m-1,11))
