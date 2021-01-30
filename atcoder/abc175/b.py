n=int(input())
d=list(map(int,input().split()))
ans = 0
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if d[i]!=d[j] and d[j]!=d[k] and d[k]!=d[i] and sum((d[i],d[j],d[k]))>max(d[i],d[j],d[k])*2:
        ans+=1
print(ans)