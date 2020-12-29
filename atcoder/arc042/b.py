import math
def dist(x1,y1,x2,y2,a1,b1):
    if x2-x1==0:
        return math.fabs(a1-x1)
    if y2-y1==0:
        return math.fabs(b1-y1)
    h=y1-((y2-y1)/(x2-x1))*x1
    w=b1+1/((y2-y1)/(x2-x1))*a1
    b2=(h+w)/2
    a2=(w-h)/2/(1/((y2-y1)/(x2-x1)))
    return math.hypot(a2 - a1, b2 - b1)

import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()

x,y=map(int,input().split())
n=int(input())
d=[]
for i in range(n):
    a,b=map(int,input().split())
    d.append((a,b))
d.append(d[0])
ans=10**9
for i in range(n):
    q,w=d[i]
    e,r=d[i+1]
    ans=min(ans,dist(q,w,e,r,x,y))
print(ans)

print(dist(-3,-4,3,4,3,0))
