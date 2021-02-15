import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,m=map(int,input().split())
d=[]
g=[[] for i in range(n)]

for i in range(m):
    d.append(tuple(map(int,input().split())))

d=sorted(d)
memo=set()
for i in range(m):
    l,r,c=d[i]
    g[l-1].append((c,r-1))
    for j in range(r):
        j=r-1-j
        if j<l:
            break
        if j in memo:
            break
        g[j].append((0,j-1))
        memo.add(j)

def dijkstra(g,st,ed):
    from heapq import heappush, heappop, heapify
    inf=10**18
    dist=[inf for i in range(len(g))]
    visited=[False for i in range(len(g))]
    dist[st]=0
    que=[]
    heappush(que,(0,st))
    while que:
        c,v=heappop(que)
        if visited[v]:
            continue
        visited[v]=True
        for x in g[v]:
            tmp=x[0]+c
            if tmp<dist[x[1]] and not visited[x[1]]:
                dist[x[1]]=tmp
                heappush(que,(tmp,x[1]))
    return dist[ed]

inf=10**18
ans=dijkstra(g,0,n-1)
print(ans if ans!=inf else -1)