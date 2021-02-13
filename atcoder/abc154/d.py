import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
p=list(map(int,input().split()))

mx=sum(p[:k])
sm=sum(p[:k])
for i in range(k,n):
    sm+=p[i]
    sm-=p[i-k]
    mx=max(mx,sm)
print((mx+k)/2)
