import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,w = map(int,input().split())
d=[]
for i in range(n):
    d.append(tuple(map(int,input().split())))

dp=[[0 for i in range(w+1)] for i in range(n)]
for i in range(n):
    for j in range(w+1):
        if j>=d[i][0]:
            dp[i][j]=max(dp[i-1][j] if i-1>=0 else 0, dp[i-1][j-d[i][0]]+d[i][1])
        else:
            dp[i][j]=dp[i-1][j] if i-1>=0 else 0

print(dp[-1][-1])
