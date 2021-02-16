n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=n
for i in range(m):
  ans-=a[i]
print(max(ans,-1))