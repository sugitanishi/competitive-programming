import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

v,t,s,d=map(int,input().split())

print('No' if v*t<=d<=v*s else 'Yes')