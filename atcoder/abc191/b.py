import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,x=map(int,input().split())
a=list(map(int,input().split()))
aa=list(filter(lambda b:b!=x,a))
print(*aa)