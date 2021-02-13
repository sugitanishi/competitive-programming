import sys
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
d=[list(map(int,input())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if d[i][j]==0 and i!=j:
            d[i][j]=999999999999

for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][j]>d[i][k]+d[k][j]:
                d[i][j]=d[i][k]+d[k][j]
c=[-1 for i in range(n)]
c[0]=0
q=deque()
q.append(0)
while q:
    v=q.popleft()
    for i in range(n):
        if i==v:
            continue
        if d[v][i]==1:
            if c[i]==c[v]:
                print(-1)
                exit()
            elif c[i]>=0:
                continue
            else:
                c[i]=1-c[v]
                q.append(i)
mx=0
for i in range(n):
    mx=max(mx,max(d[i]))
print(mx+1)
