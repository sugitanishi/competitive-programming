import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

h,w=map(int,input().split())
s=[list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        s[i][j]=0 if s[i][j]=='.' else 1
ans=0
for i in range(h-1):
    for j in range(w-1):
        d=s[i][j]+s[i+1][j]+s[i][j+1]+s[i+1][j+1]
        if d==3 or d==1:
            ans+=1
print(ans)
