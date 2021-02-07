import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

from itertools import permutations, combinations
n=int(input())
s=input()

ans = 9999
for a,b in combinations(permutations('AABBXXYY',2),2):
    a=''.join(a)
    b=''.join(b)
    ans=min([ans, len(s.replace(a,'$').replace(b,'%')), len(s.replace(b,'$').replace(a,'%'))])
print(ans)