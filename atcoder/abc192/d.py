import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

import time
def ok(s,d,n):
    tmp=0
    for i in range(len(s)):
        tmp+=int(s[i])*(d**(len(s)-i-1))
        if tmp>n:
            return False
    return True

x=input()
m=int(input())
d_min=int(sorted(set(x))[-1])+1
if len(x)==1:
    if not ok(x,d_min,m):
        print(0)
        exit()
    else:
        print(1)
        exit()
mx=d_min 
while ok(x,mx,m):
    mx*=2

l,r=d_min,mx
if not ok(x,d_min,m):
    print(0)
    exit()
while l+1<r:
    mid=(l+r)//2
    if ok(x,mid,m):
        l=mid
    else:
        r=mid
print(l-d_min+1)
