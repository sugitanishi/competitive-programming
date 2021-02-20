import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=[int(input()) for i in range(n)]
b=list(enumerate(sorted(set(a))))
c={y:x for x,y in b}
for x in a:
    print(c[x])