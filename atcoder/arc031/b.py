import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

from collections import deque

def island_count(field):
    h=10
    w=10
    dx=[1,0,-1,0,1,-1,1,-1]
    dy=[0,1,0,-1,1,1,-1,-1]
    que=deque()
    used=[[False for i in range(w)] for i in range(h)]
    count = 0
    for k in range(h):
        for j in range(w):
            if field[k][j]=='o'and not used[k][j]:
                count += 1
                used[k][j] = True
                que.append((k,j))
                while que:
                    y,x=que.popleft()
                    for i in range(4):
                        if 0<=y+dy[i]<h and 0<=x+dx[i]<w and not used[y+dy[i]][x+dx[i]] and field[y+dy[i]][x+dx[i]]=='o':
                            used[y+dy[i]][x+dx[i]] = True
                            que.append((y+dy[i],x+dx[i]))
    return count

field=[list(input()) for i in range(10)]

if island_count(field)<=1:
    print('Yes')
    exit()
for i in range(10):
    for j in range(10):
        if field[i][j]=='x':
            field[i][j]='o'
            if island_count(field)<=1:
                print('Yes')
                exit()
            field[i][j]='x'
print('No')