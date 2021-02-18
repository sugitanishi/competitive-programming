import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

a=int(input())
b=int(input())
print('EQUAL' if a==b else 'GREATER' if a>b else 'LESS')