import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
d=[]
for i in range(n):
    a,b,c=map(int,input().split())
    d.append((a,c))
    d.append((b+1,-c))

d = [(0,0)]+sorted(d)

now = 0
day = 0 
ans = 0
for i in range(len(d)):
    x,y=d[i]
    if now>k:
        ans += k*(x-day)
    else:
        ans += now*(x-day)
    now += y
    day = x
print(ans)