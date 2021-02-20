import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()

for i in range(len(s)):
    if i%2==0 and s[i].isupper() or i%2==1 and s[i].islower():
        print('No')
        break
else:
    print('Yes')

