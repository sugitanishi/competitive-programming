import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def f(n,k):
    return min(k-1,2*n-k+1) if 2<=k<=(n*2) else 0

n,k=map(int,input().split())
ans=0
for i in range(2,n*2+1):
    ans+=f(n,i)*f(n,i-k)
print(ans)

