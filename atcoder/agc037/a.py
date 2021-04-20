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
last=''
i=0
count=0
while i<len(s):
    if s[i]!=last:
        last=s[i]
        count+=1
        i+=1
    else:
        if i+1>=len(s):
            break
        last=s[i:i+2]
        count+=1
        i+=2
print(count)

