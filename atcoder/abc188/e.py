import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,m=map(int,input().split())
a=list(map(int,input().split()))

dic=[ [[],-999999999999] for i in range(n)]

for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    dic[x][0].append(y)

ans = -999999999999
for i in range(n):
    i = n-i-1
    for v in dic[i][0]:
        dic[i][1]=max(dic[i][1],dic[v][1])
    if len(dic[i][0]):
        ans=max(ans,dic[i][1]-a[i])
    dic[i][1]=max(dic[i][1],a[i])
print(ans)
