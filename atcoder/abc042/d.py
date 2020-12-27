import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
h,w,a,b=map(int,input().split())

def cmb(n,r,mod):
    if (r<0 or r>n):
        return 0
    r = min(r,n-r)
    return g1[n]*g2[r]*g2[n-r]%mod

mod = 10**9+7
N = 2*10**5
g1 = [1,1]
g2 = [1,1]
inverse = [0,1]

for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)


ans = 0
for i in range(w-b):
    ans+=cmb(h-a+b-1+i,h-a-1,mod)*cmb(w+a-b-2-i,a-1,mod)
    ans%=mod
print(ans)