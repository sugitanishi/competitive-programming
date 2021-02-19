import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=sorted(list(map(int,input().split())))
print(a[n//2]-a[n//2-1])
