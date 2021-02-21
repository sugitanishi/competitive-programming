import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,m,x,y=map(int,input().split())
g=[[] for i in range(n)]
for i in range(m):
    a,b,t,k=map(int,input().split())
    g[a-1].append((t,b-1,k))
    g[b-1].append((t,a-1,k))

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
            tmp=x[0]+(c+(x[2]-c%x[2])%x[2])
            if tmp<dist[x[1]] and not visited[x[1]]:
                dist[x[1]]=tmp
                heappush(que,(tmp,x[1]))
    return dist[ed]

ans=dijkstra(g,x-1,y-1)
print(ans if ans!=10**18 else -1)
