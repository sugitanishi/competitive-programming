#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
from math import ceil, floor, atan2, degrees
import itertools
from functools import lru_cache
from collections import deque
import cmath
inf=10**20
tau=2*cmath.pi
sys.setrecursionlimit(10000000)
input=sys.stdin.readline
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def kaku(a,b):
    return abs(a-b) if abs(a-b)<=180 else 360-abs(a-b)

def main():
    n=int(input())
    d=[tuple(map(int,input().split())) for i in range(n)]
    mx=0

    for i in range(n):
        x0,y0=d[i]
        dg=[]
        for j in range(n):
            if i==j:
                continue
            tmp=degrees(atan2(d[j][1]-y0,d[j][0]-x0))
            dg.append(tmp if tmp>=0 else 360+tmp)
        dg=sorted(dg)
        for k in range(n-1):
            l,r=0,n-1
            tmp=dg[k]+180 if dg[k]+180<360 else dg[k]-180
            while l+1<r:
                mid=(l+r)//2
                if dg[mid]<=tmp:
                    l=mid
                else:
                    r=mid
            if r<n-1:
                mx=max(mx,kaku(dg[k],dg[l]),kaku(dg[k],dg[r]))
            else:
                mx=max(mx,kaku(dg[k],dg[l]))
    print(mx)
main()