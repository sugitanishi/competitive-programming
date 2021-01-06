k=int(input())
a=7%k
for i in range(1,k+1):
    if a%k==0:
        print(i)
        break
    a=(a*10+7)%k
else:
    print(-1)
