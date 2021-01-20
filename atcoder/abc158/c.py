a,b=map(int,input().split())
for i in range(1,100000):
  if i*1.08//1-i==a and i*1.1//1-i==b:
    print(i)
    exit()
print(-1)