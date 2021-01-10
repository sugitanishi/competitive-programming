import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

memo={}
def solve(x,y):
    if (x,y) in memo:
        return memo[(x,y)]
    if x==y:
        memo[(x,y)] = 0
        return 0
    if x>y:
        memo[(x,y)] = x-y
        return x-y
    if y%2==1:
        memo[(x,y)] = min(solve(x,y-1)+1,solve(x,y+1)+1)
        return memo[(x,y)]
    memo[(x,y)] = min(solve(x,y//2)+1,y-x)
    return memo[(x,y)]

print(solve(*map(int,input().split())))
