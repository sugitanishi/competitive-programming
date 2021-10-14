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

n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    if a[i]%200==0:
        if i==0:
            print('Yes')
            print('1 2')
            print('2 1 2')
            exit()
        else:
            print('Yes')
            print('1 1')
            print(f'2 1 {i+1}')
            exit()

dp=[[0 for i in range(200)] for i in range(205)]

for i in range(n):
    for j in range(200):
        if dp[i+1][j]==0 and (j-a[i])%200==0:
            dp[i+1][j]+=1
            dp[i+1][j]=(dp[i+1][j]+dp[i][j])
        else:
            dp[i+1][j]=(dp[i+1][j]+dp[i][j])
            dp[i+1][j]=dp[i+1][j]+dp[i][(j-a[i])%200]

pi,pj=-1,-1
for i in range(n+1):
    if pi!=-1:
        break
    for j in range(200):
        if dp[i][j]>=2:
            pi,pj=i,j
            break
if (pi,pj)==(-1,-1):
    print('No')
    exit()
tpi,tpj=pi,pj
ans1=[]
ans2=[]

ans1.append(tpi)
tpj=(tpj-a[tpi-1])%200
tpi-=1

while not tpi==0:
    if dp[tpi-1][tpj]!=0 or dp[tpi][tpj]==0:
        tpi-=1
        continue
    ans1.append(tpi)
    tpj=(tpj-a[tpi-1])%200
    tpi-=1

tpi,tpj=pi,pj
while not tpi==0:
    if dp[tpi-1][tpj]!=0 or dp[tpi][tpj]==0:
        tpi-=1
        continue
    ans2.append(tpi)
    tpj=(tpj-a[tpi-1])%200
    tpi-=1
print('Yes')
print(len(ans1),*ans1[::-1])
print(len(ans2),*ans2[::-1])
