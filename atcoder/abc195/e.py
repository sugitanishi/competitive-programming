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
s=input()
x=input()

want={0}
for i in range(n)[::-1]:
    tmp = set()
    if x[i]=='T':
        for j in range(7):
            if (j*10+int(s[i]))%7 in want:
                tmp.add(j)
            if (j*10+0)%7 in want:
                tmp.add(j)
    else:
        for j in range(7):
            if (j*10+int(s[i]))%7 in want and (j*10+0)%7 in want:
                tmp.add(j)
    want=tmp
if 0 in want:
    print('Takahashi')
else:
    print('Aoki')