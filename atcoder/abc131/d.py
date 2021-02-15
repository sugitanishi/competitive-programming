import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
d={}
for i in range(n):
    a,b=map(int,input().split())
    if b in d:
        d[b]+=a
    else:
        d[b]=a
d=sorted(d.items())
t=0
for i in range(len(d)):
    t+=d[i][1]
    if d[i][0]<t:
        print('No')
        break
else:
    print('Yes')