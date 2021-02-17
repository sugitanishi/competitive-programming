import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

a,b=map(int,input().split())
print(max(400000-100000*a,0)+max(400000-100000*b,0)+(400000 if a==b==1 else 0))