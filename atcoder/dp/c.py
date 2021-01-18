import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
d=[list(map(int,input().split())) for i in range(n)]
dp=[[0, 0, 0] for i in range(n)]
dp[0]=[d[0][0], d[0][1], d[0][2]]
for i in range(1,n):
    dp[i][0]=d[i][0]+max(dp[i-1][1],dp[i-1][2])
    dp[i][1]=d[i][1]+max(dp[i-1][2],dp[i-1][0])
    dp[i][2]=d[i][2]+max(dp[i-1][0],dp[i-1][1])
print(max(dp[-1]))

