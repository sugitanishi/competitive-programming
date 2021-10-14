#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
import typing
from functools import reduce
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

s=input()
mod=10**9+7
dp = [[0 for i in range(9)] for i in range(len(s)+1)]
for i in range(len(s)+1):
    dp[i][0]=1

ss='chokudai'
for i in range(1,len(s)+1):
    for j in range(1,9):
        if s[i-1]==ss[j-1]:
            dp[i][j]+=dp[i-1][j-1]
        dp[i][j]+=dp[i-1][j]
        dp[i][j]%=mod
print(dp[-1][-1])
