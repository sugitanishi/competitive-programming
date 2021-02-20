import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

x=int(input())
n=0
while True:
    n+=100
    if x<n:
        print(n-x)
        exit()