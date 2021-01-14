# 入力高速化
# 特にこの問題のように、縦に長い入力が与えられるときに有効
import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()
######################################################

n = int(input())
s = sorted(filter(lambda x:x!=0,[int(input()) for i in range(n)]))[::-1]
q = int(input())

for i in range(q):
    k = int(input())
    print(s[k]+1 if k<len(s) else 0)

