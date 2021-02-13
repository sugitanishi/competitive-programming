import sys
from collections import deque
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
c="abcdefghij"

q=deque()
q.append(('',0))

while q:
    s,v=q.popleft()
    if len(s)==n:
        print(s)
        continue
    for i in range(v+1):
        if i!=v:
            q.append((s+c[i],v))
        else:
            q.append((s+c[i],v+1))

