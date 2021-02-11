import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
dp=[[0 for i in range(w)] for i in range(h)]
dp[0][0]=int(s[0][0]=='#')
for i in range(h):
    for j in range(w):
        if i==j==0:
            continue
        dp[i][j] = min(
            (dp[i-1][j] if i-1>=0 else 9999999999) + (1 if s[i][j]=='#' and (s[i-1][j]!='#' if i-1>=0 else True) else 0),
            (dp[i][j-1] if j-1>=0 else 9999999999) + (1 if s[i][j]=='#' and (s[i][j-1]!='#' if j-1>=0 else True) else 0)
        )
print(dp[-1][-1])
