import sys
import math
import itertools
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

def check(s):
    ret=0
    for c in '123456789':
        ret+=int(c)*10**s.count(c)
    return ret

k=int(input())
s=input()
t=input()
deck={c:k for c in '123456789'}
for c in '123456789':
    deck[c]-=s.count(c)+t.count(c)

ok=[]
for q in '123456789':
    for w in '123456789':
        if deck[q]==0 or deck[w]==0:
            continue
        if check(s.replace('#',q))>check(t.replace('#',w)):
            ok.append((q,w))
al=(9*k-8)*(9*k-9)
g=0
for a,b in ok:
    if a!=b:
        g+=deck[a]*deck[b]
    else:
        g+=max(deck[a]*(deck[b]-1),0)
print(g/al)


