import itertools
n,w=map(int,input().split())
d=[0 for i in range(2*10**5+1)]
for i in range(n):
  s,t,p=map(int,input().split())
  d[s]+=p
  d[t]-=p
print('Yes' if max(itertools.accumulate(d))<=w else 'No')