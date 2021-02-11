import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=[int(input()) for i in range(n)]
sa=sorted(a)

expect_o = set(sa[::2])
expect_e = set(sa[1::2])
print(len(expect_o-set(a[::2])))
