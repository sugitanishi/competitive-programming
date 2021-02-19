import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,m=map(int,input().split())
d=[set() for i in range(n)]
rd=[set() for i in range(n)]
for i in range(n-1+m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    d[a].add(b)
    rd[b].add(a)

p=-1
i=0
while True:
    for x in rd[i]:
        i=x
        break
    else:
        p=i
        break

from collections import deque
q=deque()
q.append(p)

ans=[0 for i in range(n)]
def check(p):
    for v in d[p]:
        rd[v].remove(p)
    for v in d[p]:
        if len(rd[v])==0 and ans[v]==0:
            ans[v]=p+1
            check(v)
check(p)
print(*ans,sep='\n')
