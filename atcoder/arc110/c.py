n=int(input())
ans=[]
used=[False for i in range(n)]
d=[i+1 for i in range(n)]
a=list(map(int,input().split()))
p=0
f=False
while True:
    for i in range(n-1):
        if f:
            i=n-2-i
        if a[i]>i+1 and a[i+1]<i+2 and not used[i]:
            ans.append(i+1)
            used[i]=True
            a[i],a[i+1]=a[i+1],a[i]
    if len(ans)==p:
        print(-1)
        break
    p=len(ans)
    if len(ans)==n-1:
        for i in range(n):
            if a[i]!=d[i]:
                print(-1)
                break
        else:
            print(*ans,sep='\n')
        break
    f = not f
