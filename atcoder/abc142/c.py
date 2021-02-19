import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
a=list(map(int,input().split()))
print(*map(lambda x:x[0]+1,sorted(enumerate(a),key=lambda x:x[1])))
