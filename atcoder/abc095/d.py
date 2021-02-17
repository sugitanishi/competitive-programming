import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,c=map(int,input().split())
r=[]
l=[]
for i in range(n):
    a,b=map(int,input().split())
    r.append((a,b))
    l.append((c-a,b))
l=l[::-1]
acm_r=[0]
acm_l=[0]
for i in range(n):
    acm_r.append(acm_r[-1]+r[i][1])
    acm_l.append(acm_l[-1]+l[i][1])
for i in range(1,n+1):
    acm_r[i]-=r[i-1][0]
    acm_l[i]-=l[i-1][0]
mxl=0
mxr=0
pl=0
pr=0
for i in range(n+1):
    if mxl<acm_l[i]:
        mxl=acm_l[i]
        pl=l[i-1][0]
    acm_l[i]=(mxl,pl)
    if mxr<acm_r[i]:
        mxr=acm_r[i]
        pr=r[i-1][0]
    acm_r[i]=(mxr,pr)
mx=0
r.insert(0,(0,0))
l.insert(0,(0,0))
for i in range(n+1):
    mx=max(acm_r[n-i][0]+acm_l[i][0]-min(acm_r[n-i][1],acm_l[i][1]),mx)
for i in range(n+1):
    mx=max(acm_l[n-i][0]+acm_r[i][0]-min(acm_l[n-i][1],acm_r[i][1]),mx)
print(mx)

