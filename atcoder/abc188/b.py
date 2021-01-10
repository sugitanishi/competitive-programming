import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
for i in range(n):
    ans += a[i]*b[i]
print('Yes' if ans==0 else 'No')