import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

h,w,n=map(int,input().split())
y,x=map(int,input().split())

s=input()
t=input()


xx,yy=x,y
for i in range(n):
    if s[i]=='U':
        yy-=1
        if yy<=0:
            print('NO')
            exit()
    if t[i]=='D' and yy+1<=h:
        yy+=1

xx,yy=x,y
for i in range(n):
    if s[i]=='D':
        yy+=1
        if yy>h:
            print('NO')
            exit()
    if t[i]=='U' and yy-1>0:
        yy-=1

xx,yy=x,y
for i in range(n):
    if s[i]=='R':
        xx+=1
        if xx>w:
            print('NO')
            exit()
    if t[i]=='L' and xx-1>0:
        xx-=1

xx,yy=x,y
for i in range(n):
    if s[i]=='L':
        xx-=1
        if xx<=0:
            print('NO')
            exit()
    if t[i]=='R' and xx+1<=w:
        xx+=1

print('YES')