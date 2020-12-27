import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()

def cmb(n,r,mod):
    if (r<0 or r>n):
        return 0
    r = min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod

mod = 998244353
N = 2*(10**5)
g1 = [1,1]
g2 = [1,1]
inverse = [0,1]

for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)


n,m,k=map(int,input().split())

if m==1:
    if k==n-1:
        print(1)
    else:
        print(0)
    exit()
ans=0
mm = (m-1)**(n-1)%mod
for i in range(k+1):
    ans+=m*mm*cmb(n-1,i,mod)
    ans%=mod
    mm*=inverse[m-1]
    mm%=mod
print(ans)