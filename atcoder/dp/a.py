n=int(input())
d=list(map(int,input().split()))
dp = [99999999999999 for i in range(n)]
dp[0]=0
for i in range(n):
    if i+1<n:
        dp[i+1]=min(dp[i+1],dp[i]+abs(d[i]-d[i+1]))
    if i+2<n:
        dp[i+2]=min(dp[i+2],dp[i]+abs(d[i]-d[i+2]))
print(dp[-1])