import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
r,s,p=map(int,input().split())
t=input()

ans=0
for i in range(k):
    d=[[r,0,0] if c=='s' else [0,s,0] if c=='p' else [0,0,p] for c in t[i::k]]
    dp=[[0 for _ in range(3)] for _ in range(len(d)+1)]
    for j in range(1,len(d)+1):
        for q in range(3):
            dp[j][q]=max(dp[j-1][(q+1)%3],dp[j-1][(q+2)%3])+d[j-1][q]
    ans+=max(dp[-1])
print(ans)
