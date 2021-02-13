import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

b,c=map(int,input().split())

if b==0:
    print(c)
    exit()
if b<0:
    q=b-c//2
else:
    q=-b-(c-1)//2
if b<0:
    w=max(-b-(c-1)//2,0)
else:
    w=max(b-c//2,0)

if b<0:
    if c<2:
        e=b
    else:
        e=min((b+(c-2)//2),-1)
else:
    e=-(b-(c-1)//2) if (b-(c-1)//2)>1 else -1

if b<0:
    r=-b+(c-1)//2
else:
    if c<4:
        r=b
    else:
        r=b+(c-2)//2
print((r-w+1)+(-q+e)+1)