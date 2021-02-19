import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

x=int(input())
a=int(input())
b=int(input())

x-=a
print(x-(x//b)*b)