import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()
print('Yes' if s.startswith('YAKI') else 'No')