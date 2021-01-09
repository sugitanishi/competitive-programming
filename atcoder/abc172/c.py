import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

import bisect
n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

for i in range(1,n):
    a[i] += a[i-1]
for i in range(1,m):
    b[i] += b[i-1]

a = [0] + a
b = [0] + b

ans = 0
for i in range(n+1):
    if a[i]>k:
        continue
    ans = max(i+bisect.bisect_right(b,k-a[i])-1, ans)

print(ans)
