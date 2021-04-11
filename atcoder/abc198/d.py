#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a,b,c=list(input()),list(input()),list(input())
alp = list(set(a)|set(b)|set(c))
if len(alp)>10:
    print('UNSOLVABLE')
    exit()
n=len(alp)

for p in itertools.permutations(map(str,range(10)), n):
    dic={al:pp  for al,pp in zip(alp,p)}
    if dic[a[0]]=='0' or dic[b[0]]=='0' or dic[c[0]]=='0':
        continue
    aa=''.join([dic[a[i]] for i in range(len(a))])
    bb=''.join([dic[b[i]] for i in range(len(b))])
    cc=''.join([dic[c[i]] for i in range(len(c))])
    if int(aa)+int(bb)==int(cc):
        print(aa)
        print(bb)
        print(cc)
        exit()
print('UNSOLVABLE')

