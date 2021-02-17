import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

from itertools import accumulate
n=int(input())
a=list(map(int,input().split()))
acm=list(accumulate(a[::2]))
memo={}
def solve(x):
    if x==1:
        return 0
    elif x==2:
        return max(a[0],a[1])
    if x in memo:
        return memo[x]
    if x%2==1:
        memo[x]=max(solve(x-2)+a[x-1],solve(x-1))
    else:
        memo[x]=max(solve(x-2)+a[x-1],acm[x//2-1])
    return memo[x]
print(solve(n))
