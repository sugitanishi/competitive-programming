import sys
sys.setrecursionlimit(10000000)
input=lambda:sys.stdin.readline().rstrip()

def popcount(n):
    return bin(n).count('1')

seglen=2**19
d=[0 for i in range(2*seglen)]

n=int(input())
s=input()

for i in range(n):
    c=i+seglen
    d[c]=1<<(ord(s[i])-ord('a'))
    while(c//2>0):
        c//=2
        d[c]=d[c*2]|d[c*2+1]

qn=int(input())
for i in range(qn):
    q,a,b=input().split()
    if q=='1':
        a=int(a)
        c=a+seglen-1
        d[c]=1<<(ord(b)-ord('a'))
        while(c//2>0):
            c//=2
            d[c]=d[c*2]|d[c*2+1]
    elif q=='2':
        a=int(a)
        b=int(b)
        ans=0
        l,r=a+seglen-1,b+seglen
        while(l<r):
            if l%2==1:
                ans|=d[l]
                l+=1
            l//=2
            if r%2==1:
                ans|=d[r-1]
                r-=1
            r//=2
        print(popcount(ans))

