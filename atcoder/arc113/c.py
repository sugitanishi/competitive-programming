import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()[::-1]

ans=0
dic={c:0 for c in 'abcdefghijklmnopqrstuvwxyz'}
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        for k in dic:
            if k!=s[i]:
                ans+=dic[k]
        dic={c:(0 if c!=s[i] else i) for c in 'abcdefghijklmnopqrstuvwxyz'}
    dic[s[i]]+=1
print(ans)
