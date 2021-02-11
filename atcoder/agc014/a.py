a,b,c=list(map(int,input().split()))
count = 0
while True:
    if count>32:
        print(-1)
        break
    if a%2 or b%2 or c%2:
        print(count)
        break
    a,b,c=b//2+c//2,a//2+c//2,b//2+c//2
    count+=1