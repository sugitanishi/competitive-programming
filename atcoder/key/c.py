import sys
sys.setrecursionlimit(1000000000)
input=lambda : sys.stdin.readline().rstrip()

mod = 998244353
N = 3
g1 = [1,1]
g2 = [1,1]
inverse = [0,1]

for i in range(2,N+1):
    g1.append((g1[-1]*i)%mod)
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g2.append((g2[-1]*inverse[-1])%mod)

h,w,k = map(int,input().split())
field = [['#' for i in range(w)] for i in range(h)]
for i in range(k):
    a,b,c = input().split()
    field[int(a)-1][int(b)-1] = c

p = 1
for i in range(h*w-k):
    p=(p*3)%mod

memo=[[-1 for i in range(w)] for i in range(h)]

memo[0][0]=p
for i in range(h):
    for j in range(w):
        if i==j==0:
            continue
        u = memo[i-1][j] if i-1>=0 else 0
        if i-1>=0 and field[i-1][j]=='#':
            u = (u*2*inverse[3])%mod
        elif i-1>=0 and field[i-1][j]=='R':
            u = 0
        l = memo[i][j-1] if j-1>=0 else 0
        if j-1>=0 and field[i][j-1]=='#':
            l = (l*2*inverse[3])%mod
        elif j-1>=0 and field[i][j-1]=='D':
            l = 0
        memo[i][j]=(u+l)%mod

print(memo[h-1][w-1])