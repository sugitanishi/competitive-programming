import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k = map(int,input().split())
print(
    1 - (
        ((n-1)/n)**3 +
        ((k-1)/n)**2 * (1/n) * 3 +
        ((n-k)/n)**2 * (1/n) * 3
    )
)