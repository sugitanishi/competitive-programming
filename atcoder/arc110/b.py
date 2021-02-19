import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

n=int(input())
t=input()
mx=10**10

if t=='1':
    print(mx*2)
elif t=='110'*(n//3):
    print(mx-(n//3)+1)
elif t in '110'*((n//3)+1):
    print(mx-((n//3)+1)+1)
elif t in '110'*((n//3)+2):
    print(mx-((n//3)+1))
else:
    print(0)
