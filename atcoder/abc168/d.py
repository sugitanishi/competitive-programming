def dijkstra(g,st,ed):
    from heapq import heappush, heappop, heapify
    inf=10**18
    dist=[inf for i in range(len(g))]
    visited=[False for i in range(len(g))]
    dist[st]=0
    que=[]
    frm=[-1 for i in range(len(g))]
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
                frm[x[1]]=v
                heappush(que,(tmp,x[1]))
    return dist,frm

n,m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    a,b = map(int, input().split())
    g[a-1].append((1, b-1))
    g[b-1].append((1, a-1))

_,frm = dijkstra(g, 0, n-1)
print('Yes')
for i in range(1, n):
    print(frm[i]+1)
