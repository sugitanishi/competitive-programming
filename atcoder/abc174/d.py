import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
c=input()

print(c[:c.count('R')].count('W'))