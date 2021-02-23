import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

x,y,a,b=map(int,input().split())
ans=0
while x*a<x+b and x*a<y:
    ans+=1
    x*=a
print(ans+((y-1-x)//b))


