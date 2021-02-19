import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

from collections import deque
tmp=input()
s=deque()
for c in tmp:
    s.append(c)
q=int(input())
rev_count=0
for i in range(q):
    query=input()
    if query=='1':
        rev_count+=1
    else:
        _,f,c=query.split()
        f=int(f)
        if (f-1+rev_count)%2==0:
            s.appendleft(c)
        else:
            s.append(c)
print(*(s if rev_count%2==0 else list(s)[::-1]),sep='')
