n,m=map(int,input().split())
d=[0 for i in range(m)]
for i in range(n):
    x=list(map(int,input().split()))
    for j in range(1,x[0]+1):
        d[x[j]-1]+=1

count=0
for i in range(m):
    if d[i]==n:
        count+=1
print(count)