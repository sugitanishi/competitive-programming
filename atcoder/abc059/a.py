import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

a,b,c=input().split()
print((a[0]+b[0]+c[0]).upper())