#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor
import itertools
from functools import lru_cache
from collections import deque
import random
import time
inf=10**20
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

start_time=time.time()
sy,sx=map(int,input().split())
cell_group=[list(map(int,input().split())) for i in range(50)]
cell_point=[list(map(int,input().split())) for i in range(50)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
dcoms=['R','D','L','U']

def evaluate(data):
    h,w,_com,point=data
    return -(point+cell_point[h][w])

def dfs(h,w,point,used):
    if time.time()-start_time>1.82:
        print(ans[::-1])
        exit()
    target=[]
    point+=cell_point[h][w]
    for i in range(4):
        next_h=h+dy[i]
        next_w=w+dx[i]
        if not 0<=next_h<50 or not 0<=next_w<50:
            continue
        if not (cell_group[next_h][next_w] in used):
            target.append((next_h,next_w,dcoms[i],point))
    if len(target)==0:
        return ('',point)
    target=sorted(target, key=evaluate)
    fixed_ret=('',0)

    i=0
    next_h,next_w,dcom,point=target[i]
    used.add(cell_group[next_h][next_w])
    ret=dfs(next_h,next_w,point,used)
    used.remove(cell_group[next_h][next_w])
    fixed_ret=(ret[0]+dcom,ret[1])
    
    if len(target)>=2 and random.random()<0.12:
        i=random.randint(1,len(target)-1)
        next_h,next_w,dcom,point=target[i]
        used.add(cell_group[next_h][next_w])
        ret=dfs(next_h,next_w,point,used)
        used.remove(cell_group[next_h][next_w])
        if fixed_ret[1]<ret[1]:
            fixed_ret=(ret[0]+dcom,ret[1])

    return fixed_ret

mx_point=0
while True:
    used=set()
    used.add(cell_group[sy][sx])
    ans_command,point=dfs(sy,sx,0,used)
    if mx_point<point:
        ans=ans_command
        mx_point=point

