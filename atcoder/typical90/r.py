#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
import cmath
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def pos(l,t,now):
    rotate=cmath.rect(1,-2*cmath.pi*(now/t))*complex(0,-1)+complex(0,1)
    return (0,rotate.real*(l/2),rotate.imag*(l/2))


t=int(input())
l,x,y=map(int,input().split())
q=int(input())
for i in range(q):
    a,b,c=pos(l,t,int(input()))
    new_e8=complex(0,c)
    new_choku=complex(abs((complex(x,y)-complex(0,b))),0)
    print(math.degrees(-cmath.phase(new_choku-new_e8)))



