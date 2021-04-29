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

h,w,y,x=map(int,input().split())
field=[input() for i in range(h)]

dx=[1,0,-1,0,1,-1,1,-1]
dy=[0,1,0,-1,1,1,-1,-1]


ans=0
for i in range(4):
    now_x,now_y=x-1,y-1
    while 0<=now_y+dy[i]<h and 0<=now_x+dx[i]<w and field[now_y+dy[i]][now_x+dx[i]]!='#':
        now_y+=dy[i]
        now_x+=dx[i]
        ans+=1
print(ans+1)
