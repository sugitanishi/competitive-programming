import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k,s=map(int,input().split())

ans=[10**9 if s!=10**9 else 10**9-1 for i in range(n)]
ans[:k]=[s for i in range(k)]
print(*ans)
