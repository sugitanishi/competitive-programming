import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

import math

n,m=map(int,input().split())
a=[0]+sorted(list(map(int,input().split())))+[n+1]
d=[]
for i in range(1,m+2):
    if a[i]-a[i-1]-1!=0:
        d.append(a[i]-a[i-1]-1)
ans=0
if len(d)==0:
    print(0)
    exit()
st=min(d)
for x in d:
    ans+=math.ceil(x/st)
print(ans)
