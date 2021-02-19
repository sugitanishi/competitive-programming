import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=list(map(int,input().split()))
m=1000
d=[]
f=a[0]
for i in range(1,n):
    if a[i-1]>a[i]:
        d.append((f,a[i-1]))
        f=a[i]
d.append((f,a[-1]))

for i in range(len(d)):
    m=m-d[i][0]*(m//d[i][0])+(m//d[i][0])*d[i][1]
print(m)
