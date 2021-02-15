import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

s=input()
print(len(s)//2-s.count('p'))
