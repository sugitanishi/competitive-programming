import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
mn=99999999999999999
for i in range(n):
    a,p,x=map(int,input().split())
    mn=min(p,mn) if x-a>0 else mn
print(mn if mn!= 99999999999999999 else -1)

