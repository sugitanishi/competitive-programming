import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

a,b=map(int,input().split())
print('Yes' if abs(a-b)<=2 else 'No')