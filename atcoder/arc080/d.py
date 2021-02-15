import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))
ans=[[0 for i in range(w)] for i in range(h)]
p=0
for i in range(h):
    for j in range(w):
        if i%2==1:
            j=w-1-j
        ans[i][j]=p+1
        a[p]-=1
        if a[p]==0:
            p+=1
for i in range(h):
    print(*ans[i])
