import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n,k=map(int,input().split())
s = input()

count = 0
i = 0
d = []
while i<n:
    if s[i]=='0':
        count-=1
    else:
        count+=1
    if i+1<n and s[i]!=s[i+1]:
        d.append(count)
        count = 0
    i+=1
d.append(count)

l,r=0,0
count=0 if d[0]>=0 else 1
sm=abs(d[0])
ans=abs(d[0])
while True:
    if r+1<len(d):
        r+=1
        sm+=abs(d[r])
        count+=1 if d[r]<0 else 0
    else:
        break
    while count>k:
        sm-=abs(d[l])
        count-=1 if d[l]<0 else 0
        l+=1
    if count<=k:
        ans = max(ans,sm)
print(ans)
