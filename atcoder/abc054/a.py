import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

d=[2,3,4,5,6,7,8,9,10,11,12,13,1]
a,b=map(int,input().split())
print('Alice' if d.index(a)>d.index(b) else 'Draw' if d.index(a)==d.index(b) else 'Bob')
