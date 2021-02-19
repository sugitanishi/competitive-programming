import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()
k=int(input())

r='abcdefghijklmnopqrstuvwxyz'
p=0
l=1
ans=set()
while p < len(r):
    f=False
    for i in range(len(s)):
        if s[i]==r[p]:
            ans.add(s[i:i+l])
            f=True
    if f and l<k:
        l+=1
    else:
        p+=1
        l=1
print(sorted(ans)[k-1])
