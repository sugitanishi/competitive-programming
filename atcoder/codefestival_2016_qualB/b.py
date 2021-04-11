#☆𝒐𝒎𝒂𝒋𝒊𝒏𝒂𝒊☆#
import sys
import math
import itertools
from functools import lru_cache
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
'''''✂'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

n,a,b=map(int,input().split())
s=input()
p=0
bp=1
for i in range(n):
    if s[i]=='a':
        print('Yes' if a+b>p else 'No')
        if a+b>p:
            p+=1
    if s[i]=='b':
        print('Yes' if a+b>p and bp<=b else 'No')
        if a+b>p and bp<=b:
            p+=1
            bp+=1
    if s[i]=='c':
        print('No')