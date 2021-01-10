import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int,input().split()))
l,r=max(a[:len(a)//2]),max(a[len(a)//2:])

print(a.index(min(l,r))+1)