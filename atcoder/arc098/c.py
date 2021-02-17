import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
s=input()
count=s[1:].count('E')
mn=count
for i in range(1,n):
    if s[i] == 'E':
        count-=1
    if s[i-1] == 'W':
        count+=1
    mn=min(mn,count)
print(mn)