import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
s=set(map(int,input().split()))
print('YES' if len(s)==n else 'NO')