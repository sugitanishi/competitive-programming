#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
import time
import random
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
FIELD_LEN = 10000

def make_sq_len(n):
    return int((99999999//n)**0.5)

n=int(input())
in_data=[tuple(map(int,input().split())) for i in range(n)]
mx_ans_count = 0
_hw = make_sq_len(n)
s=time.time()
first = True
while time.time()-s<4:
    if first:
        hw = _hw
        first = False
    else:
        hw = _hw + random.randint(-200,200)
    if not 0<hw<10000:
        continue
    if FIELD_LEN%hw==0:
        hw-=1
    cell={(i,j):[] for i in range(FIELD_LEN//hw) for j in range(FIELD_LEN//hw)}
    for i in range(FIELD_LEN//hw):
        for j in range(FIELD_LEN//hw):
            for k in range(n):
                x,y,r=in_data[k]
                if i*hw<=x<(i+1)*hw and j*hw<=y<(j+1)*hw:
                    cell[(i,j)].append(k)

    ans=[(i,9999,i+1,10000) for i in range(n)]
    ans_count=0
    for i in range(FIELD_LEN//hw):
        for j in range(FIELD_LEN//hw):
            if len(cell[(i,j)])==0:
                continue
            cell[(i,j)]=sorted(cell[(i,j)], key = lambda x:in_data[x][2])
            k=cell[(i,j)][0]
            ad=in_data[k]
            if ad[2]>hw*hw:
                continue
            l,r,u,d=ad[0]-hw*i,ad[0]-hw*i+1,ad[1]-hw*j,ad[1]-hw*j+1
            while (r-l)*(d-u)<ad[2] and l-1>=0:
                l-=1
            while (r-l)*(d-u)<ad[2] and r+1<hw:
                r+=1
            while (r-l)*(d-u)<ad[2] and u-1>=0:
                u-=1
            while (r-l)*(d-u)<ad[2] and d+1<hw:
                d+=1
            l,r,u,d=l+hw*i,r+hw*i,u+hw*j,d+hw*j
            ans[k]=(l,u,r,d)
            ans_count+=1
    if ans_count>mx_ans_count:
        ans_all=ans[:]
        mx_ans_count = ans_count

for i in range(n):
    print(*ans_all[i])
