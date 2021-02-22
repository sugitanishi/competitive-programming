import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

a,b,x=map(int,input().split())
if (a**2*b)-x<=(a**2*b)/2:
    c=2*((a**2*b)-x)/(a**2)
    print(math.degrees(math.atan2(c,a)))
else:
    c=2*x/b/a
    print(math.degrees(math.atan2(b,c)))
