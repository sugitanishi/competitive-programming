n=int(input())
d=[]
for i in range(n):
  a,b=map(int,input().split())
  d.append(1 if a==b else 0)
for i in range(n-2):
  if sum(d[i:i+3])==3:
    print('Yes')
    break
else:
  print('No')