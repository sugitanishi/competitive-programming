import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def dijkstra(st):
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
    return dist

n,m=map(int,input().split())
f=[[99999999999999 for i in range(n)] for i in range(n)]
g=[set() for i in range(n)]
gg=[set() for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    f[a-1][b-1]=min(f[a-1][b-1],c)
    g[a-1].add(b-1)
    gg[b-1].add(a-1)
for i in range(n):
    g[i]=[(f[i][v],v) for v in g[i]]
    gg[i]=[(f[v][i],v) for v in gg[i]]
for i in range(n):
    if len(gg[i])==0:
        pass
    dist=dijkstra(i)
    mn = f[i][i]
    for cc,v in gg[i]:
        if v==i:
            continue
        mn=min(mn,dist[v]+cc)
    print(mn if mn!=99999999999999 else -1)


