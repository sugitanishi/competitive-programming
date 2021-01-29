ans=0
n=int(input())
d=list(map(int,input().split()))
mx=0
for i in range(len(d)):
  if mx<=d[i]:
    mx=d[i]
  else:
    ans+=mx-d[i]
print(ans)