import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

from functools import reduce
n=int(input())
a=list(map(int,input().split()))

def gcd(x,y):
    while x != 0:
        x,y=y%x,x
    return y

print(reduce(gcd,a))
