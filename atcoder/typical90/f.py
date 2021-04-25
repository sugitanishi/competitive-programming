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

n,k=map(int,input().split())
s=input()
table=[[-1 for i in range(n)] for i in range(26)]

for j in reversed(range(n)):
    for i in range(26):
        if ord(s[j])==ord('a')+i:
            table[i][j]=j
        elif j!=n-1:
            table[i][j]=table[i][j+1]

j=0
ans=[]
while len(ans)<k:
    for i in range(26):
        if table[i][j]>=0 and n-table[i][j]+len(ans)>=k:
            ans.append(chr(ord('a')+i))
            j=table[i][j]+1
            break
print(''.join(ans))

