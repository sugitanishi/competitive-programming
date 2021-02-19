import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()
ans=0
for i in range(len(s)):
    if s[i]=='U':
        ans+=len(s)-1-i
        ans+=i*2
    else:
        ans+=(len(s)-1-i)*2
        ans+=i
print(ans)
