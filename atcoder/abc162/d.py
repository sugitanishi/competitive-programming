import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
s=input()
r=[]
g=[]
b=[]
for i in range(n):
    if s[i]=='R':
        r.append(i)
    if s[i]=='G':
        g.append(i)
    if s[i]=='B':
        b.append(i)
d=sorted([r,g,b],key=lambda x:len(x))
d[2]=set(d[2])
r,g,b=d
ans=0
for i in range(len(r)):
    for j in range(len(g)):
        diff = abs(r[i]-g[j])
        mn,mx=min(r[i],g[j]),max(r[i],g[j])
        ans+=len(b) - len({x for x in [mn-diff, mx+diff, ((mn+mx)//2) if (mn+mx)%2==0 else None] if x in b})
print(ans)
