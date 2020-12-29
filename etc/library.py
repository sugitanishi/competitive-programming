#再起深さの変更と高速インプット magic
import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

#入力受け取り
map(int,input().split())

#整数受け取り
int(input())

#Yes/No
print('Yes' if True else 'No')

#8方向dxdy
dx=[1,0,-1,0,1,-1,1,-1]
dy=[0,1,0,-1,1,1,-1,-1]

#gcd,lcm
def gcd(x,y):
    while x != 0:
        x,y=y%x,x
    return y
def lcm(x,y):
    return (x * y)//gcd(x, y)

#プリム法-最小全域木
from heapq import heappush, heappop, heapify
used = [0]*N
que = [(c, w) for w, c in G[0]]
used[0] = 1
heapify(que)

ans = 0
while que:
    cv, v = heappop(que)
    if used[v]:
        continue
    used[v] = 1
    ans += cv
    for w, c in G[v]:
        if used[w]:
            continue
        heappush(que, (c, w))

#エラトステネス
def eratosthenes(n):
    prime_table = [False,False,True]+[False if i%2!=0 else True for i in range(n-2)]
    i=3
    while i*i<=n:
        if prime_table[i]:
            j=i*i
            while j<=n:
                prime_table[j]=False
                j+=i
        i+=2
    return prime_table

#最大流問題
class Graph:
    class edge:
        pass
    def __init__(self,n):
        self._graph=[[] for i in range(n)]

class MaxFlow(Graph):
    class edge:
        def __init__(self,to,cap,rev):
            self.to=to
            self.cap=cap
            self.rev=rev

    def __init__(self,n):
        super().__init__(n)
        self._used=[False for i in range(n)]

    def add(self,f,to,cap):
        self._graph[f].append(self.edge(to,cap,len(self._graph[to])))
        self._graph[to].append(self.edge(f,0,len(self._graph[f])-1))

    def dfs(self,v,t,f):
        if v==t:
            return f
        self._used[v]=True
        for e in self._graph[v]:
            if not self._used[e.to] and e.cap>0:
                d=self.dfs(e.to,t,min(f,e.cap))
                if d>0:
                    e.cap-=d
                    self._graph[e.to][e.rev].cap+=d
                    return d
        return 0

    def max_flow(self,s,t,inf=99999999):
        _flow=0
        while 1:
            self._used = [False for i in range(len(self._graph))]
            _f=self.dfs(s,t,inf)
            if _f==0:
                break
            _flow+=_f
        return _flow

#UnionFind(旧)
class UnionFind:
    def __init__(self, n):
        self.p=[i for i in range(n)]
        self.r=[0 for i in range(n)]
    
    def root(self,x):
        if self.p[x]==x:
            return x
        else:
            self.p[x] = self.root(self.p[x])
            return self.p[x]
    
    def uni(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if(x==y):
            return
        if self.r[x]<self.r[y]:
            self.p[x]=y
        else:
            self.p[y]=x
            if self.r[x]==self.r[y]:
                self.r[x]+=1
    
    def same(self,x,y):
        return self.root(x)==self.root(y)

#重み付きUF
class P_UnionFind:
    def __init__(self, n):
        self.p=[i for i in range(n)]
        self.r=[0 for i in range(n)]
        self.d=[0 for i in range(n)]
    def root(self,x):
        if self.p[x]==x:
            return x
        else:
            tmp = self.root(self.p[x])
            self.d[x] += self.d[self.p[x]]
            self.p[x] = tmp
            return self.p[x]
    
    def weight(self,x):
        self.root(x)
        return self.d[x]

    def diff(self,x,y):
        if self.root(x)==self.root(y):
            return self.weight(y)-self.weight(x)
        else:
            return '?'

    def uni(self,x,y,w):
        w+=self.weight(x)
        w-=self.weight(y)
        x=self.root(x)
        y=self.root(y)
        if(x==y):
            return
        if self.r[x]<self.r[y]:
            self.p[x]=y
            self.d[x]=-w
        else:
            self.p[y]=x
            self.d[y]=w
            if self.r[x]==self.r[y]:
                self.r[x]+=1
    
    def same(self,x,y):
        return self.root(x)==self.root(y)

#UnionFind(新)
class UnionFind:
    def __init__(self, n):
        self.data=[-1 for i in range(n)]

    def root(self,x):
        if self.data[x]<0:
            return x
        else:
            self.data[x]=self.root(self.data[x])
            return self.data[x]

    def uni(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if(x==y):
            return
        if self.data[y]<self.data[x]:
            x,y=y,x
        self.data[x]+= self.data[y]
        self.data[y] = x

    def same(self,x,y):
        return self.root(x)==self.root(y)

    def size(self,x):
        return -self.data[self.root(x)]

#field4方向幅優先探索
from collections import deque
dx=[1,0,-1,0,1,-1,1,-1]
dy=[0,1,0,-1,1,1,-1,-1]
que=deque()
que.append((1,1))
while que:
    y,x=que.popleft()
    for i in range(4):
        if 0<=y+dy[i]<h and 0<=x+dx[i]<w:
            pass

#Graph(行列)
class Graph:
    _inf = 99999999

    def __init__(self, node_num):
        self._path = [[Graph._inf for i in range(node_num)] for i in range(node_num)]
        self._node_num = node_num

    def view(self,table=False):
        if not table:
            i = 0
            for d in self._path:
                flag = 0
                for node in range(self._node_num):
                    if d[node] != Graph._inf:
                        if flag == 0:
                            print('%4d ->' % i, node, 'cost:' + str(d[node]))
                            flag = 1
                        else:
                            print('     ->', node, 'cost:' + str(d[node]))
                _tmp = set(d)
                if not (len(_tmp)==1 and list(_tmp)[0]==99999999):
                    print('')
                i += 1
        else:
            for d in self._path:
                for n in d:
                    if n == Graph._inf:
                        print('  inf',end = '')
                    else:
                        print(' %4d' % n,end = '')
                print('')

    def update(self,f,d,cost,directed=False):
        self._path[f][d] = cost
        if not directed:
            self._path[d][f] = cost

#Dijkstra(行列)
class Dijkstra(Graph):
    def __init__(self, node_num):
        super().__init__(node_num)
        self._distance = [Graph._inf for i in range(node_num)]
        self._used = [False for i in range(node_num)]
        self._before = [-1 for i in range(node_num)]
        self._route = []
        self._before_update_start = -1
        self._before_update_end = -1

    def shortest_path(self, start):
        if self._before_update_start != start:
            self._distance = [Graph._inf for i in range(self._node_num)]
            self._used = [False for i in range(self._node_num)]
            self._before_update_start = start
            self._distance[start] = 0
            while True:
                m = (Graph._inf, -1, -1)
                for d in zip(self._distance, self._used, range(self._node_num)):
                    if d[1] == False and d[0]< m[0]:
                        m = d
                if m[2] == -1:
                    break
            
                self._used[m[2]] = True

                for i in range(self._node_num):
                    self._distance[i] = min(self._distance[i], self._distance[m[2]] + self._path[m[2]][i])
                    if self._distance[i] == self._distance[m[2]] + self._path[m[2]][i]:
                        self._before[i] = m[2]
        return self._distance

    def shortest_route(self, start, end):
        if self._before_update_start == start and self._before_update_end == end:
            return self._route
        elif self._before_update_start == start:
            Dijkstra._route(self, self._before, start, end)
            self._before_update_start = start
            self._before_update_end = end
            return self._route
        else:
            Dijkstra.shortest_path(self, start, end)
            return self._route

    def shortest_route_cost(self, start, end):
        if self._before_update_start == start and self._before_update_end == end:
            return self._distance[end]
        elif self._before_update_start == start:
            self._before_update_start = start
            self._before_update_end = end
            return self._distance[end]
        else:
            Dijkstra.shortest_path(self, start)
            self._before_update_start = start
            self._before_update_end = end
            return self._distance[end]

    def _route(self, before_list, start, end):
        p = end
        self._route = []
        while True:
            self._route.append(p)
            if p == start:
                self._route = self._route[::-1]
                break
            else:
                p = before_list[p]

g = Dijkstra(int(input()))


#dijkstra関数
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

#LIS長
import bisect
LIS = [a[0]]
for i in range(len(a)):
    if a[i]>LIS[-1]:
        LIS.append(a[i])
    else:
        LIS[bisect.bisect_left(LIS,a[i])] = a[i]

#汎用セグ木
class SegTree:
    '''Segment Tree:
    Data structure to answer queries on segments of a sequence.
    '''
    def __init__(self,n,init_num,func):
        '''Create a segment tree.
        :param n: Size
        :type n: int or float (number)
        :param init_num: Initialization number
        :type init_num: int or float (number)
        :param func: Function to use
        :type func: function
        '''
        self.func=func
        self.init_num=init_num
        self.size = 2**(len(bin(n-1))-2)*2-1
        self.tree = [init_num for i in range(self.size)]
     
    def data(self):
        '''Return data.
        '''
        return self.tree[self.size//2:]
 
    def update(self,i,x,update_func):
        '''Update the i-th data by update_func.
            example:
            a[i]<-update_func(a[i],x)
        '''
        i=self.size//2+i
        self.tree[i]=update_func(self.tree[i],x)
        while 1:
            i=(i-1)//2
            self.tree[i]=self.func(self.tree[i*2+1],self.tree[i*2+2])
            if i<=0:
                break
 
    def _check(self,s,t,l,r,_p=0):
        if s<=l and r<=t:
            return self.tree[_p]
        elif r<s or t<l:
            return self.init_num
        else:
            return self.func(self._check(s,t,l,l+(r-l)//2,_p*2+1),self._check(s,t,l+(r-l)//2+1,r,_p*2+2))
 
    def find(self,s,t):
        '''Answer query on [s,t]segment
        '''
        return self._check(s,t,0,self.size//2)

#組み合わせ(逆元使用)
def cmb(n,r,mod):
    if (r<0 or r>n):
        return 0
    r = min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod

mod = 10**9+7
N = 10**5
g1 = [1,1]
g2 = [1,1]
inverse = [0,1]

for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)


#高速input
import sys
input=lambda : sys.stdin.readline().rstrip()

#素因数分解
def prime_factor(n):
    x=2
    lim=int(n**0.5)
    factors=[]
    while n!=1 and x<=lim:
        if n%x==0:
            n//=x
            factors.append(x)
        else:
            x+=1
    if n!=1:
        factors.append(n)
    return factors