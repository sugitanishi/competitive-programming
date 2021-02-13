import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def check(x,y):
    a,t,c,g=y[0]-x[0],y[1]-x[1],y[2]-x[2],y[3]-x[3]
    return a==t and c==g

n,s=input().split()
n=int(n)
d=[[0,0,0,0],[0,0,0,0]]
d[1]['ATCG'.find(s[0])]+=1
for i in range(1,n):
    nxt=d[-1][:]
    nxt['ATCG'.find(s[i])]+=1
    d.append(nxt)

ans=0
for i in range(n+1):
    for j in range(i):
        if check(d[i],d[j]):
            ans+=1
print(ans)
