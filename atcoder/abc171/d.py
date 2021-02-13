import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=list(map(int,input().split()))
q=int(input())
d=[0 for i in range(10**5+1)]
for x in a:
    d[x]+=1
sm=0
for i in range(len(d)):
    sm+=i*d[i]
for i in range(q):
    b,c=map(int,input().split())
    sm-=d[b]*b
    sm+=d[b]*c
    d[c]+=d[b]
    d[b]=0
    print(sm)
