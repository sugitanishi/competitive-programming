import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())

def ok(x,n):
    return n>=(x+1)*x//2

l,r=0,n+1
while l+1<r:
    mid=(l+r)//2
    if ok(mid,n+1):
        l=mid
    else:
        r=mid

print(n-l+1)
