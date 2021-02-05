import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
f=sorted(list(map(int,input().split())))[::-1]

def check(a,f,d,k):
    ans=0
    for i in range(len(a)):
        ans+=max((a[i]-d//f[i]),0)
    return ans<=k

l=-1
r=10**12+1
while l+1<r:
    mid = (l+r)//2
    if check(a,f,mid,k):
        r=mid
    else:
        l=mid
print(r)
