import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

t=int(input())

for i in range(t):
    l,r=map(int,input().split())
    if r-l*2+1>0:
        print((1+(r-l*2+1))*(r-l*2+1)//2)
    else:
        print(0)
