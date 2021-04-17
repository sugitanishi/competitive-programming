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

def diff(a,b):
    ret=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            ret+=1
    return ret
s=input()
print(min(diff(s,'10'*10**5),diff(s,'01'*10**5)))