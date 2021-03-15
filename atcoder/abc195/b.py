#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

a,b,w=map(int,input().split())

w*=1000

x,y=int(math.ceil(w/b)),int(math.floor(w/a))

if x>y:
    print('UNSATISFIABLE')
else:
    print(x,y)
