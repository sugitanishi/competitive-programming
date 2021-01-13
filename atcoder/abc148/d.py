import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int,input().split()))
if 1 not in a:
  print(-1)
  exit()

max_len = 0
p = 1
for i in range(n):
  if a[i] == p:
    max_len += 1
    p += 1
print(len(a) - max_len)