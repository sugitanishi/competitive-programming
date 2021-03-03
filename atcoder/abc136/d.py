#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

s=input()
d=s.replace('LR','L,R').split(',')

ans=[]
for ss in d:
    r=ss.count('R')
    l=ss.count('L')
    for i in range(len(ss)):
        if i+1<len(ss) and ss[i]+ss[i+1]=='RL':
            ans.append(int(math.ceil(r/2))+l//2)
        elif i-1>=0 and ss[i-1]+ss[i]=='RL':
            ans.append(r//2+int(math.ceil(l/2)))
        else:
            ans.append(0)
print(*ans)