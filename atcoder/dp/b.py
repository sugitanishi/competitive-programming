import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
d=list(map(int,input().split()))
dp = [99999999999999 for i in range(n)]
dp[0]=0
for i in range(n):
    for j in range(1,k+1):
        if i+j<n:
            dp[i+j]=min(dp[i+j],dp[i]+abs(d[i]-d[i+j]))
print(dp[-1])