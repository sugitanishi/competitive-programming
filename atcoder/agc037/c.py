import time
import math

n=int(input())
d=list(map(int,input().split()))
a=list(map(int,input().split()))

count=0
st=time.time()
ok=[False for i in range(n)]

while time.time()-st<1:
    f=False
    for i in range(n):
        if ok[i]:
            continue
        if a[i-1]+a[i-(n-1)]<a[i]:
            if (a[i]-d[i])%(a[i-1]+a[i-(n-1)])==0:
                count+=(a[i]-d[i])//(a[i-1]+a[i-(n-1)])
                ok[i]=True
                a[i]=d[i]
            else:
                tmp=math.ceil((a[i]-max((a[i-1]+a[i-(n-1)]),d[i]))/(a[i-1]+a[i-(n-1)]))
                count+=tmp
                a[i]-=tmp*(a[i-1]+a[i-(n-1)])
            f=True
    if not f:
        if a==d:
            print(count)
            break
        else:
            print(-1)
            break
else:
    print(-1)