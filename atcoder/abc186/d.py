n=int(input())
a=sorted(map(int,input().split()),key=lambda x:-x)
sm=sum(a)
ans=0
for i in range(n-1):
  sm-=a[i]
  ans+=a[i]*(n-1-i)-sm
print(ans)